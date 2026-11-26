"""ローカル閲覧ビューア用の簡易サーバー（標準ライブラリのみ）。

- outputs/ 配下の Markdown を一覧・取得する
- logs/ 配下の作業ログを取得する
- README.md、CLAUDE.md、docs/ 配下の Markdown を取得する
- 127.0.0.1 にのみバインドする（外部からは接続できない）

使い方:
    start-viewer.bat（Windows）または start-viewer.command（Mac）をダブルクリック
    手動で起動する場合（リポジトリのルートで実行）:
        python apps/viewer/server.py [ポート番号]
    起動時にブラウザが自動で開く。
"""

import json
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

VIEWER_DIR = Path(__file__).resolve().parent
REPO_ROOT = VIEWER_DIR.parent.parent
OUTPUTS_DIR = REPO_ROOT / "outputs"
LOGS_DIR = REPO_ROOT / "logs"
DOCS_DIR = REPO_ROOT / "docs"
DEFAULT_PORT = 8765


def title_from_lines(lines):
    """行の並びから、最初の見出し（# で始まる行）をタイトルとして返す。無ければ None。"""
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return None


def read_title(path):
    """Markdown ファイルのタイトルを返す。読めない・見出しが無い場合は None。"""
    try:
        with path.open(encoding="utf-8") as f:
            return title_from_lines(f)
    except (OSError, UnicodeDecodeError):
        return None


def list_notes():
    """outputs/ 配下の .md ファイル一覧を返す。"""
    notes = []
    for path in sorted(OUTPUTS_DIR.rglob("*.md")):
        rel = path.relative_to(OUTPUTS_DIR).as_posix()
        parts = rel.split("/")
        notes.append({
            "path": rel,
            "category": parts[0] if len(parts) > 1 else "",
            "name": path.name,
            "title": read_title(path) or path.name,
            "mtime": path.stat().st_mtime,
        })
    return notes


def resolve_note(rel):
    """相対パスを outputs/ 配下の .md ファイルに限定して解決する。不正なら None。"""
    if not rel or not rel.endswith(".md"):
        return None
    target = (OUTPUTS_DIR / rel).resolve()
    try:
        target.relative_to(OUTPUTS_DIR.resolve())
    except ValueError:
        return None
    return target if target.is_file() else None


def doc_paths():
    """ヘルプで閲覧できるファイル（README.md、CLAUDE.md、docs/ 配下の .md）の相対パス一覧。"""
    paths = [REPO_ROOT / "README.md", REPO_ROOT / "CLAUDE.md"]
    paths += sorted(DOCS_DIR.glob("*.md"))
    return [p.relative_to(REPO_ROOT).as_posix() for p in paths if p.is_file()]


def list_docs():
    """ヘルプで閲覧できるファイルの一覧（タイトル付き）を返す。"""
    return [{"path": rel, "name": Path(rel).name,
             "title": read_title(REPO_ROOT / rel) or Path(rel).name}
            for rel in doc_paths()]


def resolve_doc(rel):
    """相対パスを doc_paths() の対象ファイルに限定して解決する。不正なら None。"""
    return REPO_ROOT / rel if rel in doc_paths() else None


def make_snippet(text, q):
    """本文から検索語の前後を切り出す。本文に無ければ空文字。"""
    idx = text.lower().find(q)
    if idx < 0:
        return ""
    start = max(0, idx - 20)
    end = min(len(text), idx + len(q) + 50)
    body = " ".join(text[start:end].split())
    return ("…" if start > 0 else "") + body + ("…" if end < len(text) else "")


def search_files(q):
    """タイトル・パス・本文に検索語を含む .md ファイルを探し、[{path, snippet}] で返す。

    outputs/ 配下は outputs/ からの相対パス、ヘルプ対象は リポジトリからの相対パス。
    両者のパスは重ならないため、1つのリストにまとめる。
    """
    q = q.strip().lower()
    if not q:
        return []
    targets = [(p.relative_to(OUTPUTS_DIR).as_posix(), p) for p in sorted(OUTPUTS_DIR.rglob("*.md"))]
    targets += [(rel, REPO_ROOT / rel) for rel in doc_paths()]
    result = []
    for rel, path in targets:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        title = title_from_lines(text.splitlines()) or path.name
        snippet = make_snippet(text, q)
        if snippet or q in rel.lower() or q in title.lower():
            result.append({"path": rel, "snippet": snippet})
    return result


def read_worklogs():
    """logs/ 配下の作業ログ（.txt）を新しい日付順で返す。"""
    logs = []
    for path in sorted(LOGS_DIR.glob("*_workLog.txt"), reverse=True):
        lines = path.read_text(encoding="utf-8").splitlines()
        logs.append({"file": path.name, "lines": [l for l in lines if l.strip()]})
    return logs


class ViewerHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(VIEWER_DIR), **kwargs)

    def log_message(self, format, *args):
        # 標準の接続ログは抑制する
        pass

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_md(self, resolver, rel):
        """resolver で解決できた Markdown を {path, content} で返す。解決できなければ 404。"""
        target = resolver(rel)
        if target is None:
            return self.send_json({"error": "not found"}, status=404)
        return self.send_json({"path": rel, "content": target.read_text(encoding="utf-8")})

    def do_GET(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)

        if url.path == "/" or url.path == "/index.html":
            self.path = "/index.html"
            return super().do_GET()

        if url.path == "/api/notes":
            return self.send_json(list_notes())

        if url.path == "/api/note":
            return self.send_md(resolve_note, query.get("path", [""])[0])

        if url.path == "/api/docs":
            return self.send_json(list_docs())

        if url.path == "/api/doc":
            return self.send_md(resolve_doc, query.get("path", [""])[0])

        if url.path == "/api/search":
            return self.send_json(search_files(query.get("q", [""])[0]))

        if url.path == "/api/worklog":
            return self.send_json(read_worklogs())

        self.send_json({"error": "not found"}, status=404)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT
    url = f"http://127.0.0.1:{port}/"
    try:
        server = HTTPServer(("127.0.0.1", port), ViewerHandler)
    except OSError:
        print(f"ポート {port} は使用中のため起動できません。")
        print("既にビューアが起動している場合は、そのブラウザを開いてください。")
        sys.exit(1)
    print(f"ビューアを起動しました: {url}  （終了は Ctrl+C）")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n終了しました。")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
