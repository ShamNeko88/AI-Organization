# 変換先: Confluence Cloud（新エディタ）

## 1. 状態
暫定。公式ドキュメントで確認できた範囲だけで作った。実際に貼って確認するまで「検証済み」にしない。
確認日: 2026-11-26

## 2. 出力形式
- ファイル名: post_confluence.md
- 中身: 標準的なMarkdown（プレーンテキスト）。HTMLは使わない。
- 手動の挿入が必要な装飾には、目印の行を入れる（6を参照）。

## 3. 貼り付け方
1. post_confluence.md をテキストエディタ（メモ帳など）で開き、全体をコピーする。
2. Confluence のページを編集画面にし、本文に貼り付ける。
3. 変換されずに記号がそのまま残った行は、入力ショートカット（下の4）で手入力し直す。
   - 貼り付け前に、メモ帳などで一度プレーンテキストにすると、変換される場合がある（Atlassian の課題管理 CONFCLOUD-66301 に、この回避策が書かれている。現在の動作は未確認）。
4. 目印の行（【手動:…】）を探し、6の手順で装飾を手動で挿入して、目印の行を削除する。
- 旧エディタ（legacy editor）の「挿入 > マークアップ」と、wiki マークアップ（{info} など）は、使えない。旧エディタは 2026-04-01 に完全に廃止された。

## 4. 変換表
公式の「入力時の Markdown ショートカット」に載っている記法だけを使う。
貼り付けで同じ範囲が変換されるかは、公式の記載がなく、未確認。

- 見出し: `#` 〜 `######` の後に半角スペース
- 太字: `**太字**`
- 斜体: `*斜体*`
- 取り消し線: `~~取り消し線~~`
- インラインコード: `` `code` ``
- 箇条書き: 行頭を `* `（アスタリスクと半角スペース）にする。公式の一覧に `-` はないため、`*` に統一する。
- 番号付きリスト: `1. `
- 引用: `> `
- コードブロック: ``` で囲む
- 区切り線: `---`
- リンク: `[タイトル](URL)`
- 表: Markdown の表の記法は、公式に記載がない。変換されるかは未確認。
  - Markdown の表のまま出力する。行頭にスペースを入れない。空のセルをハイフンだけにしない（行頭スペース付きの表やハイフンだけのセルで、エディタが固まる報告がある。出典はコミュニティの報告で、本文は未確認）。
  - 変換されなかった場合は、表の挿入（ツールバーまたはスラッシュコマンド）で作る。paste_guide.md に、表がある旨を書く。
- 画像: Markdown の画像記法は、貼り付けでの扱いが未確認。画像の位置に目印（【手動:画像「ファイル名」】）を入れ、手動で挿入する。

## 5. 装飾
Markdown では表現できない。すべて手動で挿入する（6を参照）。
元の文章の意味に応じて、次のように当てはめる。

- 注意・警告 → パネル（warning）
- 補足・参考情報 → パネル（info）
- メモ → パネル（note）
- ポイント・成功・完了 → パネル（success）
- エラー・禁止 → パネル（error）
- 長い補足や詳細（折りたたみたい部分） → 展開（expand）
- 状態の表示（完了、進行中など） → ステータス
- ページ冒頭の目次 → 目次マクロ
- 強調したい語 → 文字色またはハイライト
- 左右に並べたい内容 → レイアウト（2〜5列）

## 6. 手動の作業が必要なもの
変換後のファイルには、次の形式の目印の行を入れる。

- ブロック: 開始に `【手動:種類 ここから】`、終了に `【手動:ここまで】` を、それぞれ単独の行で入れる。
  - 例: `【手動:パネル(warning) ここから】` ～ `【手動:ここまで】`
- 1行で済むもの: `【手動:ステータス(Green)「完了」】`、`【手動:目次】`、`【手動:画像「ファイル名」】`

挿入方法（公式のドキュメントで確認済み）:

- パネル: `/panel` と入力する。プリセットは info、note、error、success、warning の5種類。背景色は20色から選べる。
  - tip のプリセットは、新エディタに載っていない。tip の内容は、別のプリセット（success など）に置き換える。
- 展開: `/expand` と入力する。
- ステータス: `/status` と入力する。色は Grey（既定）、Red、Yellow、Green、Blue の5色。
- 目次: `/` を入力し、マクロ名で絞り込んで選ぶ。見出しを作ったあとに挿入する。
- 文字色・ハイライト: 文字を選択し、ツールバーの「Text and highlight color」から色を選ぶ。
- レイアウト: `/layout` と入力する（Insert メニューの Layouts からも選べる）。列は2〜5列。

## 7. 制約・注意
- 貼り付けた Markdown の変換範囲（表、入れ子のリスト、`-` の箇条書きなど）は、公式の情報がなく、未確認。
- 変換後は Confluence の形式で保存され、Markdown としては再編集できない。
- 目印の行は、貼り付け後に必ず削除する。

## 8. 出典と未確認の点
出典（Atlassian 公式。いずれも 2026-11-26 に確認）:
- https://support.atlassian.com/confluence-cloud/docs/keyboard-shortcuts-markdown-and-autocomplete/
- https://support.atlassian.com/confluence-cloud/docs/available-markdown-commands/
- https://support.atlassian.com/confluence-cloud/docs/insert-elements-into-a-page/
- https://support.atlassian.com/confluence-cloud/docs/insert-the-status-macro/
- https://support.atlassian.com/confluence-cloud/docs/insert-the-table-of-contents-macro/
- https://support.atlassian.com/confluence-cloud/docs/format-text/
- https://support.atlassian.com/confluence-cloud/docs/create-and-manage-layouts/
- https://support.atlassian.com/confluence-cloud/docs/insert-confluence-wiki-markup/
- https://support.atlassian.com/confluence-cloud/docs/faq-understanding-legacy-editor-deprecation/
- https://jira.atlassian.com/browse/CONFCLOUD-66301

未確認の点:
- 貼り付けた Markdown が、どの記法まで変換されるか（公式の記事がない）。
- 「Markdown として貼り付け」専用の機能があるか。
- 目次のスラッシュコマンドの正確な名前（公式は「/ のあとにマクロ名」としか書いていない）。
- 画像、入れ子のリストの貼り付け時の扱い。
