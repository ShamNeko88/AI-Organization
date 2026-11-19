
# AI-Organization

Claude Codeを活用した、用途別のAIエージェントを作って育てる場所。
議論系（意見を出し合う）、調査系（情報を集めて検証する）、メンター（学習・業務の相談と記録）などを
まとめ、必要に応じてエージェントとスキルを追加していく。
GitHubで構成を管理し、別の環境でも再利用する。

## 基本的な使い方

Claude Codeを本リポジトリのルートで起動する。
start-claude.bat（Windows）または start-claude.command（Mac）をダブルクリックでも起動できる。
Macで初回に動かない場合は、chmod +x start-claude.command を実行する。

- /multi-perspective：複数の視点から課題を分析する
- /research-it-news：IT・セキュリティニュースを集めてまとめる（期間・テーマを指定可）
- /mentor：メンターとして相談に乗ってもらう（「メンター終了」で解除）
- /mentor-note：相談内容をノートに保存する
- /setup-ai-team：AI組織の構築・改善を支援する

## エージェント一覧

- realist：現実主義者。実現可能性、費用対効果、リスク
- idealist：理想主義者。創造性、可能性、長期的な価値
- critic：批判・検証担当。前提条件、反証、見落とし
- research-collector：情報収集担当。出典付きで情報を集める
- research-checker：裏取り担当。出典・日付・整合性を確認する

## スキル一覧

- multi-perspective：議論系3エージェントの意見を比較して結論を出す
- setup-ai-team：AI組織の構築・改善を支援する
- research-it-news：IT・セキュリティニュースの収集・裏取り・要約
- mentor：呼んだときだけメンターとして応答する
- mentor-note：学習ノートを保存する
- mentor-quiz：ノートから問題を作り出題する
- mentor-review：期間を指定してノートを振り返る
- mentor-organizer：「その他」のノートを整理する

## 運用のコツ

- 話題が変わったら /clear する（文脈が混ざると精度が落ちる）。
- メンター使用中は、/clear の前に /mentor-note で保存する（保存していない内容は消える）。
- 長く続けたと感じたら /context で使用量を確認する。
- エージェントやスキルを追加したときは、この README の一覧と docs/ を更新する。

## 詳細（docs/）

- [docs/agents.md](docs/agents.md)：エージェントの役割と判断基準、モデル設定、フォルダ構成、命名ルール、運用方針
- [docs/skills.md](docs/skills.md)：各スキルの使い方
- [docs/mentor.md](docs/mentor.md)：メンターの使い方
- [docs/changelog.md](docs/changelog.md)：改善履歴
