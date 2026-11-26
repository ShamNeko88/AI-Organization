"""ローカル閲覧ビューア用の簡易サーバー（標準ライブラリのみ）。

- outputs/ 配下の Markdown を一覧・取得する
- logs/ 配下の作業ログを取得する
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
DEFAULT_PORT = 8765


def read_title(path):
    """Markdown の最初の見出し（# で始まる行）をタイトルとして返す。無ければ None。"""
    try:
        with path.open(encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    return line[2:].strip()
    except (OSError, UnicodeDecodeError):
        pass
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

    def do_GET(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)

        if url.path == "/" or url.path == "/index.html":
            self.path = "/index.html"
            return super().do_GET()

        if url.path == "/api/notes":
            return self.send_json(list_notes())

        if url.path == "/api/note":
            rel = query.get("path", [""])[0]
            target = resolve_note(rel)
            if target is None:
                return self.send_json({"error": "not found"}, status=404)
            text = target.read_text(encoding="utf-8")
            return self.send_json({"path": rel, "content": text})

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
