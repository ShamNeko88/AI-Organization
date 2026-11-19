---
name: research-it-news
description: IT・セキュリティの最新ニュースを定義済みの情報源から集め、裏取りして、影響の大きい順にまとめる。期間とテーマは指定できる。
disable-model-invocation: true
argument-hint: "[期間 例: 直近2週間] [テーマ・前提 例: クラウド中心、自社はAWS利用]"
---

# 目的
IT・セキュリティの動向を、情報源リストに基づいて定期的に把握できる形にまとめる。
単発の調査ではなく、ニュース収集の型として使う。

# 引数と既定値
- 期間: 指定がなければ「直近1週間」
- テーマ: 指定がなければ「セキュリティ中心（インシデント、脆弱性、注意喚起）＋クラウド・IT全般」
- 影響の前提: 引数で指定された利用環境・業務の前提に従う。指定がなければ一般的な企業IT担当者を想定し、その旨を成果物に明記する。

# 使うエージェント
新しいエージェントは作らない。既存の次の2つを使う。
- research-collector: 情報源から収集する
- research-checker: 出典・日付・整合性を裏取りする

# 実行手順

## STEP 1：条件を確定する
期間、テーマ、影響の前提を確定し、一行で復唱する。

## STEP 2：過去の成果物を確認する
outputs/research/*_it-news/topic_summary.md を読み、すでに載せた項目を把握する。
- 同じ項目は載せない。
- 続報があるものは「続報」として、新しい情報だけを載せる。

## STEP 3：収集する（research-collector）
下の情報源リストを起点に、期間内の情報を集めるよう依頼する。
- 目的、期間、テーマ、情報源リスト、STEP 2 の既出項目を伝える。
- 情報源リスト外の情報源を使った場合は、その旨を明記させる。
- 各項目に、出典URLと情報の日付を付けさせる。

## STEP 4：裏取りする（research-checker）
収集結果を渡し、出典・日付・整合性を確認させる。
- 各項目を「確認済み」「未確認・続報待ち」に分けさせる。
- 期間外の項目、出典が確認できない項目は除外または未確認とする。

## STEP 5：まとめる
- 影響の大きい順に並べる（重要度の高いものを上位に）。判断は「影響の前提」に従う。
- 「確認済み」と「未確認・続報待ち」を明確に分けて書く。特にインシデント系は、確認できた事実と未確認の情報を混ぜない。
- 事実、推測、意見を区別する。
- 各項目に出典URLと日付を付ける。

## STEP 6：保存する
outputs/research/yyyymmdd_it-news/topic_summary.md に保存する。
- 同名のフォルダ・ファイルがある場合は上書きせず、追記するか別名にするかをユーザーに確認する。
- 次の項目を載せる: 結論、使用したエージェント、根拠、参考サイト。
- 期間、テーマ、影響の前提、使用した情報源リストの状態（暫定/確定）を冒頭に書く。

## STEP 7：報告する
保存先と、上位の項目の要点を3行以内で伝える。

# 成果物の形式

```markdown
# IT・セキュリティニュース yyyy-mm-dd

- 期間: 
- テーマ: 
- 影響の前提: 
- 情報源リスト: 暫定 / 確定

## 結論
要点と、優先して対応・確認すべきもの。

## 確認済み（影響の大きい順）
### 1. 項目名
- 内容: 
- 影響: 
- 出典: URL（日付）

## 未確認・続報待ち
### 1. 項目名
- 現時点で分かっていること: 
- 未確認の点: 
- 出典: URL（日付）

## 使用したエージェント
## 根拠
## 参考サイト
```

# 情報源リスト（暫定）
注意: このリストは暫定。Claude Code が提案し、URLの到達確認（HTTP 200、またはリダイレクト先で応答）だけ行った。
内容の信頼性や網羅性は、利用者の確認が取れるまで確定扱いにしない。
確定したら、この見出しを「情報源リスト（確定）」に変え、注意書きを更新する。

公的機関・脆弱性情報
- JPCERT/CC 注意喚起: https://www.jpcert.or.jp/at/
- IPA 重要なセキュリティ情報: https://www.ipa.go.jp/security/security-alert/
- 内閣サイバーセキュリティセンター（現サイト）: https://www.cyber.go.jp/
- JVN（脆弱性対策情報）: https://jvn.jp/
- CISA サイバーセキュリティ勧告: https://www.cisa.gov/news-events/cybersecurity-advisories
- CISA 既知の悪用された脆弱性カタログ: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- NVD（米国脆弱性データベース）: https://nvd.nist.gov/

ベンダー公式
- Microsoft Security Update Guide: https://msrc.microsoft.com/update-guide
- AWS セキュリティ情報: https://aws.amazon.com/security/security-bulletins/
- AWS What's New: https://aws.amazon.com/new/
- Google Cloud セキュリティ情報: https://docs.cloud.google.com/support/bulletins
- Azure Updates: https://azure.microsoft.com/en-us/updates/

ITニュースサイト
- Krebs on Security: https://krebsonsecurity.com/
- ITmedia NEWS セキュリティ: https://www.itmedia.co.jp/news/feature/security
- Security NEXT: https://www.security-next.com/

到達確認できなかった候補（リストには含めない）
- BleepingComputer、The Hacker News: 自動アクセスが拒否（403）され、確認できなかった。

# 注意
- URLを推測で追加しない。リストにない情報源を使うときは、実在とアクセスを確認する。
- 確認していない情報を「確認済み」にしない。
- 定期実行の設定はしない。呼んだときだけ実行する。
