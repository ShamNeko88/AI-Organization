# ローカル閲覧ビューア

## 概要

outputs/ の成果物（Markdown）と logs/ の作業ログを、ブラウザで閲覧するための簡易ビューア。
閲覧専用で、ファイルの編集や削除はしない。

## 起動方法

- Windows：start-viewer.bat をダブルクリックする。
- Mac：start-viewer.command をダブルクリックする。初回に動かない場合は、chmod +x start-viewer.command を実行する。
- 手動：リポジトリのルートで `python apps/viewer/server.py [ポート番号]` を実行する。

起動するとブラウザが自動で開く。終了は、起動したウィンドウで Ctrl+C を押す。
標準のポートは 8765。使用中の場合は起動せず、メッセージが表示される。

## 閲覧できるもの

上部のタブは3つ。

- 「成果物」タブ：outputs/ 配下の .md ファイル（議論、調査、メンターの記録）
- 「ツール」タブ：一覧の先頭のボタンで、次の2つを切り替える。
  - 一問一答：outputs/mentor/quiz/questions/ の問題集を、1問ずつ解く形式で表示する（詳細は mentor.md）。初期表示はこちら。
  - 作業ログ：logs/ 配下の作業ログ（yyyymmdd_workLog.txt）
- 「ヘルプ」タブ：README.md、CLAUDE.md、docs/ 配下の .md ファイル

## 検索

- 「成果物」「ヘルプ」タブの検索窓で、ファイル名・タイトル・本文を検索できる（大文字と小文字は区別しない）。
- 本文に一致した場合は、一覧に一致箇所の抜粋が出る。
- 「ツール」タブでは検索窓は出ない。

## 構成

- apps/viewer/server.py：簡易サーバー（Python標準ライブラリのみ）
- apps/viewer/index.html：画面
- start-viewer.bat / start-viewer.command：起動用ファイル

## 注意

- Python 3 が必要。追加のインストールは不要。
- 127.0.0.1 にのみ接続を受け付けるため、他の端末からは見えない。
- 返すのは、outputs/ 配下の .md ファイル、README.md、CLAUDE.md、docs/ 配下の .md ファイルだけ。それ以外のファイルは取得できない。
- outputs/mentor/ や logs/ は個人的な内容を含むため、ポートを外部に公開しない。
