# スキル

スキルは .claude/skills/スキル名/SKILL.md で定義する。
/スキル名 で呼び出し、必要に応じて議題や追加条件を指定する。
※ 実際の動作には、Claude Codeによるエージェントの呼び出しが必要。

## multi-perspective

議論系の3エージェント（realist / idealist / critic）に独立した分析を依頼し、
意見の比較と最終結論の作成を行う。調査系エージェントは呼び出さない。

使い方：/multi-perspective 議題

## setup-ai-team

AI組織の構築、エージェントの追加、役割や指示の改善を支援する。
作業前に変更内容を説明し、承認を得てからファイルを作成・変更する。

使い方：/setup-ai-team 追加したい役割や改善したい点

## research-it-news

IT・セキュリティの最新ニュースを、SKILL.md 内の情報源リストから集める。
research-collector で収集し、research-checker で出典・日付・整合性を裏取りして要約する。
手動で呼んだときだけ動く。定期実行はしない。

使い方：/research-it-news [期間] [テーマ・影響の前提]

- 既定の期間：直近1週間
- 既定のテーマ：セキュリティ中心（インシデント、脆弱性、注意喚起）＋クラウド・IT全般
- 影響の前提：指定した利用環境・業務に合わせて、影響の大きい順に並べる

出力

- outputs/research/yyyymmdd_it-news/topic_summary.md
- 結論、使用したエージェント、根拠、参考サイトを載せる
- 「確認済み」と「未確認・続報待ち」を分けて書く
- 過去の outputs/research/*_it-news/ を確認し、掲載済みの項目は重複して載せない

情報源リスト

- 公的機関、脆弱性情報、ベンダー公式、ITニュースサイトを SKILL.md 内に持つ。
- 現在は暫定リスト。URLの到達確認のみ済みで、内容の確認と確定は利用者が行う。
- 確定したら SKILL.md の見出しと注意書きを更新する。

## mentor 系スキル

/mentor、/mentor-note、/mentor-quiz、/mentor-review、/mentor-organizer。
使い方は [mentor.md](mentor.md) を参照。
