# 変換先: WordPress（Cocoon）

## 1. 状態
暫定。Cocoon 公式リポジトリのソース（master、2026-11-26 時点）で確認した記法だけで作った。
実際の WordPress で貼って表示を確認するまで「検証済み」にしない。
Cocoon のバージョンごとの差は、未確認。

## 2. 出力形式
- ファイル名: post_cocoon.html
- 中身: HTML（Cocoon の class を使う）。
- 1つの要素（ボックス、段落、リストなど）は、HTML の中で改行せず、1行に収める（3の理由を参照）。要素どうしの間は、改行してよい。

## 3. 貼り付け方
1. 推奨: ブロックエディタで「カスタムHTML」ブロックを追加し、post_cocoon.html の中身を貼り付ける。
   - 本文にブロックが含まれていると、WordPress は改行を p / br に自動変換しない（WordPress 本体のソースで確認済み）。
2. クラシックエディタ（テキストタブ）に貼る場合は、改行が p / br に変換される。1要素1行にしてあるのは、このため。
3. 【差し替え:…】の目印がある箇所（画像のURL、吹き出しのアイコン、ボタンのリンク先）を、実際の値に直す。
4. 元のMarkdownの見出し（# の1行目）は、投稿のタイトル欄に入れる。post_cocoon.html には含めない。

## 4. 変換表
- 見出し: `##` → `<h2>`、`###` → `<h3>`、`####` → `<h4>`（`#` はタイトルとして扱う。3の4を参照）。見出し専用の装飾 class は確認できていないので、付けない。
- 段落: `<p>…</p>`
- 太字: `<strong>…</strong>`、斜体: `<em>…</em>`
- 取り消し線: `<span class="strike">…</span>`
- インラインコード: `<code>…</code>`
- 箇条書き: `<ul><li>…</li></ul>`、番号付き: `<ol><li>…</li></ol>`（1行に収める）
- リンク: `<a href="URL">文字</a>`
- 画像: `<img src="【差し替え:画像URL（元の記載: 元のパス）】" alt="説明">`。WordPress のメディアにアップロードしたURLに差し替える。
- コードブロック: `<pre><code>…</code></pre>`。中の `<` `>` `&` は `&lt;` `&gt;` `&amp;` にする。この要素だけは、コード内の改行を保つ。
- 引用: `<blockquote><p>…</p></blockquote>`
- 区切り線: `<hr>`
- 表: `<table><thead>…</thead><tbody>…</tbody></table>`。専用の装飾 class は確認できていないので、付けない。
- 本文中の `<` `>` `&` は、エスケープする。

## 5. 装飾
ソースで確認できたものだけを書く。元の文章の意味に応じて、次のように当てはめる。

### 5-1. ボックス
- 補足・情報: `<div class="information-box"><p>…</p></div>`
- 質問・疑問: `<div class="question-box"><p>…</p></div>`
- 注意・警告: `<div class="alert-box"><p>…</p></div>`
- 色付きの汎用ボックス: `primary-box`（濃い水色）、`success-box`（薄い緑）、`info-box`（薄い青）、`warning-box`（薄い黄）、`danger-box`（薄い赤）。書式は同じ（`<div class="success-box"><p>…</p></div>`）。
- メモ: `<div class="memo-box"><p>…</p></div>`
- コメント・発言の引用: `<div class="comment-box"><p>…</p></div>`
- OK・推奨: `<div class="ok-box common-icon-box"><p>…</p></div>`
- NG・非推奨: `<div class="ng-box common-icon-box"><p>…</p></div>`
- 良い例・悪い例: `good-box`、`bad-box`（書式は ok-box と同じ。`common-icon-box` を併記する）
- ok / ng / good / bad / profile のボックスに `common-icon-box` を併記するのは、エディタ側の定義に合わせたもの。単独で使ったときの表示は未確認。

### 5-2. 白抜きボックス・付箋
- 白抜き（色のみ）: `<div class="blank-box bb-yellow"><p>…</p></div>`
  - 色: bb-red / bb-pink / bb-purple / bb-blue / bb-green / bb-orange / bb-yellow / bb-brown / bb-grey / bb-black
- ラベル付き: `<div class="blank-box bb-tab bb-point bb-red"><p>…</p></div>`
  - 必ず「class を div の最初の属性にし、`blank-box bb-tab bb-ラベル` の順」に書く（ラベルの文字は、公開ページの表示時に自動で挿入されるため）。
  - ラベル: bb-check / bb-comment / bb-point / bb-tips / bb-hint / bb-pickup / bb-bookmark / bb-memo / bb-download / bb-break / bb-ok / bb-ng / bb-good / bb-bad / bb-profile / bb-amazon
  - 色は、ラベルの後ろに `bb-red` などを足す（省略できる）。
- 付箋風: `<div class="blank-box sticky st-yellow"><p>…</p></div>`（st-yellow / st-red / st-blue / st-green）

### 5-3. 文字装飾（`<span class="…">…</span>`）
- 太字: bold、赤字: red、太い赤字: bold-red（`bold red` でも有効）、赤アンダー: red-under
- 青字: blue、太い青字: bold-blue
- 黄色マーカー: marker、黄色アンダーマーカー: marker-under
- 赤・青のマーカー: marker-red / marker-blue、アンダー: marker-under-red / marker-under-blue
- バッジ: `badge`。色付きは `badge badge-red` のように併記する（red / pink / purple / blue / green / yellow / brown / grey）
- キーボード操作: `keyboard-key`
- ルビ: `<ruby>漢字<rt>かんじ</rt></ruby>`

### 5-4. トグル（開閉）ボックス
長い補足や詳細（折りたたみたい部分）に使う。JavaScript は不要。
```
<div class="toggle-wrap toggle-box block-box cocoon-block-toggle"><input id="toggle-checkbox-cv1" class="toggle-checkbox" type="checkbox"><label class="toggle-button" for="toggle-checkbox-cv1">見出し</label><div class="toggle-content"><p>本文</p></div></div>
```
- id と for は、同じ値にし、ファイル内で重複しないよう連番にする（cv1、cv2、…）。ページ内で他のトグルと重ならないよう、`cv` を接頭辞にしている。
- 色の class（tb-*）は、使い方が未確認なので付けない。

### 5-5. 見出し付きボックス（caption-box / label-box / tab-caption-box）
ポイントや手順などを、見出し付きで目立たせたいときに使う。3種は同じ構造で、接頭辞だけが違う。
```
<div class="caption-box block-box cocoon-block-caption-box"><div class="caption-box-label block-box-label box-label"><span class="caption-box-label-text block-box-label-text box-label-text">見出し</span></div><div class="caption-box-content block-box-content box-content"><p>本文</p></div></div>
```
- label-box、tab-caption-box は、`caption-box` の部分を `label-box`、`tab-caption-box` に置き換える。
- 色の class は、確認できていないので付けない。

### 5-6. ボタン
リンク先を示すときに使う。
`<div class="btn-wrap btn-wrap-red btn-wrap-l"><a href="【差し替え:リンク先URL】">文言</a></div>`
- 色: red / pink / purple / blue / green / yellow / orange / brown / grey / black / white
- サイズ: `btn-wrap-m`、`btn-wrap-l`（s は CSS にない）

### 5-7. 吹き出し
会話形式の文章や、一言コメントにだけ使う。
```
<div class="speech-wrap sbs-stn sbp-l sbis-cn cf"><div class="speech-person"><figure class="speech-icon"><img src="【差し替え:アイコン画像URL】" alt="名前" class="speech-icon-image" width="92" height="92"></figure><div class="speech-name">名前</div></div><div class="speech-balloon"><p>本文</p></div></div>
```
- sbs-（形）: stn（標準）、flat、line、think
- sbp-（位置）: l（左）、r（右）
- sbis-（アイコンの形）: sn、sb、cn、cb
- `sb-id-{ID}` は、管理画面で登録した吹き出しの ID。手書きでは付けない。アイコン画像のURLと名前は、自分で入れる。
- アイコンの画像URLが分からない場合は、使わない。

## 6. 手動の作業が必要なもの
次の目印は、貼り付け後に実際の値へ直す。目印は paste_guide.md に一覧で書く。
- 【差し替え:画像URL…】: WordPress のメディアにアップロードして、URLに差し替える。
- 【差し替え:アイコン画像URL】: 吹き出しのアイコン画像のURL。
- 【差し替え:リンク先URL】: ボタンのリンク先。

## 7. 制約・注意
- 見出し、表、アイコンリスト（iconlist-box）は、専用の装飾 class の値が確認できていないので使わない。
- 吹き出しの短縮コード（ショートコード）は、確認した範囲では見つからなかった。
- 目次のショートコード（[toc]）は、確認していないので使わない。目次は、Cocoon の設定で自動表示する。
- Cocoon の最新版でない場合、一部の class が存在しない可能性がある。

## 8. 出典と未確認の点
出典（Cocoon 公式リポジトリ https://github.com/xserver-inc/cocoon の master、2026-11-26 に確認）。以下は、https://raw.githubusercontent.com/xserver-inc/cocoon/master/ からの相対パス:
- lib/admin-tinymce-qtag.php（クイックタグ。ボックス、文字装飾、白抜きボックス）
- style.css（各 class の定義）
- lib/page-speech-balloon/speech-balloon-func.php（吹き出し）
- blocks/src/block/toggle-box/save.js（トグル）
- blocks/src/block-universal/caption-box/save.js、label-box、tab-caption-box（見出し付きボックス）
- blocks/src/helpers.js、style.css の btn 系（ボタン）
- lib/page-speed-up/minify-html.php（白抜きボックスのラベルの自動挿入）
- WordPress 本体（wordpress-develop の trunk）の wp-includes/default-filters.php と blocks.php（wpautop の扱い）

未確認の点:
- 実際の WordPress と Cocoon での表示（bb-label の自動挿入、ok-box の単独使用、ボタンの表示など）。
- 見出し、表、アイコンリストの専用 class。
- caption-box 系の色の class。
- Cocoon 公式マニュアル（wp-cocoon.com）には、HTML の例が載っていない。貼り付け時の公式の注意書きも、確認できていない。
