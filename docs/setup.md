# セットアップ

本リポジトリを自分の環境で使うための前提と注意点。

## 前提条件

- Claude Code がインストールされ、ログイン済みであること（有効な契約またはAPI利用が必要）。
- Git（リポジトリを取得する場合）。
- Web検索が使えること。research-collector と /research-it-news が情報収集に使う。

## 取得と起動

1. リポジトリをクローンする。
2. ルートフォルダで claude を起動する。
   start-claude.bat（Windows）または start-claude.command（Mac）でも起動できる。
3. Macで初回に動かない場合は、chmod +x start-claude.command を実行する。

## 言語

エージェント、スキル、ドキュメントはすべて日本語で書かれている。
他の言語で使う場合は、.claude/ 配下のMarkdownと CLAUDE.md を翻訳・調整する。

## モデル設定

research-checker と critic は model: opus を指定している。
契約によって使えない場合は、各ファイルの model を inherit に変更する。
詳細は [agents.md](agents.md) の「モデル設定」を参照。

## 共通ルール（CLAUDE.md）

ルート直下の CLAUDE.md は、本リポジトリで起動したときの共通ルール。
個人用の設定（ユーザー全体の CLAUDE.md や settings.local.json）は含まれない。
必要に応じて自分のルールに書き換える。

## 保存先

成果物は outputs/ に保存される。中身はGit管理外（フォルダ維持用の .gitkeep のみ管理）。
