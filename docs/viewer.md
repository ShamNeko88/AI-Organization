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

- outputs/ 配下の .md ファイル（議論、調査、メンターの記録）
- logs/ 配下の作業ログ（yyyymmdd_workLog.txt）

## 構成

- apps/viewer/server.py：簡易サーバー（Python標準ライブラリのみ）
- apps/viewer/index.html：画面
- start-viewer.bat / start-viewer.command：起動用ファイル

## 注意

- Python 3 が必要。追加のインストールは不要。
- 127.0.0.1 にのみ接続を受け付けるため、他の端末からは見えない。
- outputs/ 配下の .md ファイルだけを返す。それ以外のファイルは取得できない。
- outputs/mentor/ や logs/ は個人的な内容を含むため、ポートを外部に公開しない。
