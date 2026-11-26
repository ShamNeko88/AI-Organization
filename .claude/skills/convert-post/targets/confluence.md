# 変換先: Confluence Cloud（新エディタ）

## 1. 状態
暫定。公式ドキュメントで確認できた範囲だけで作った。実際に貼って確認するまで「検証済み」にしない。
確認日: 2026-11-26

## 2. 出力形式
- ファイル名: post_confluence.md
- 中身: 標準的なMarkdown（プレーンテキスト）と絵文字。HTMLは使わない。
- 貼り付けたあとの手作業が必要な装飾は、使わない（6を参照）。

## 3. 貼り付け方
1. post_confluence.md をテキストエディタ（メモ帳など）で開き、全体をコピーする。
2. Confluence のページを編集画面にし、本文に貼り付ける。
3. 変換されずに記号がそのまま残った行は、入力ショートカット（下の4）で手入力し直す。
   - 貼り付け前に、メモ帳などで一度プレーンテキストにすると、変換される場合がある（Atlassian の課題管理 CONFCLOUD-66301 に、この回避策が書かれている。現在の動作は未確認）。
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
  - 変換されなかった場合は、表の挿入（ツールバーまたはスラッシュコマンド）で作る。元に表がある場合は、完了報告で「表は貼り付けで変換されない可能性がある」と伝える。
- 画像: 貼り付けでは入らない可能性が高い（未確認）。元の画像記法をそのまま残し、完了報告で「画像は別途挿入が必要」と伝える。

## 5. 装飾
Confluence のパネルなどは、貼り付けでは作れない（6を参照）。
代わりに、引用、太字、区切り線、絵文字で、見た目に変化をつける。すべて貼り付けるだけで使える。
元の文章の意味に応じて、次のように当てはめる。

- 注意・警告: `> ⚠️ **注意** 本文`
- 補足・参考情報: `> ℹ️ **補足** 本文`
- ポイント: `> 💡 **ポイント** 本文`
- OK・推奨・完了: `> ✅ 本文`
- NG・禁止・エラー: `> ❌ 本文`
- メモ: `> 📝 **メモ** 本文`
- 重要な語句: `**語句**`
- セクションの切れ目: `---`
- 見出しの先頭の絵文字: 結論は `📌`、手順は `🔧`、注意事項は `⚠️` など、見出しの内容に合うものを1つだけ付けてよい（`## 📌 結論`）。付けすぎない。

- 絵文字は、通常の文字として貼り付く想定だが、Confluence での表示は未確認。
- 引用の中の太字と絵文字の組み合わせも、実際に貼っての確認はしていない。

## 6. 使わない装飾（手作業が必要なため）
次の装飾は、貼り付けだけでは作れず、画面での挿入が必要になる。手作業を減らすため、使わない。
- パネル（`/panel`）、展開（`/expand`）、ステータス（`/status`）、目次マクロ
- 文字色・ハイライト（ツールバーで選ぶ）
- レイアウト（`/layout`）

## 7. 制約・注意
- 貼り付けた Markdown の変換範囲（表、入れ子のリスト、`-` の箇条書きなど）は、公式の情報がなく、未確認。
- 変換後は Confluence の形式で保存され、Markdown としては再編集できない。

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
