
# AI-Organization

Claude Codeを活用した、用途別のAIエージェントを作って育てる場所。

現在は、意見を出し合う議論系(現実主義者・理想主義者・批判担当)と、
情報を集めて検証する調査系のエージェントを持つ。
今後も必要に応じて、エージェントとスキルを追加していく。

## 1. 目的

- 用途別のAIエージェントを作り、継続的に改善する
- 議論系:異なる価値観を持つAIに意見を出させ、偏りの少ない意思決定を支援する
- 調査系:情報を出典付きで集め、裏取りを行う
- GitHubで構成を管理し、別の環境でも再利用する

## 2. フォルダ構成

```text
AI-Organization/
├── README.md
├── CLAUDE.md
├── start-claude.bat       # Windows用の起動ファイル
├── start-claude.command   # Mac用の起動ファイル
├── .claude/
│   ├── agents/
│   │   ├── realist.md
│   │   ├── idealist.md
│   │   ├── critic.md
│   │   ├── research-collector.md
│   │   └── research-checker.md
│   └── skills/
│       ├── setup-ai-team/
│       │   └── SKILL.md
│       └── multi-perspective/
│           └── SKILL.md
└── outputs/
    ├── discussion/        # 議論系の成果物(yyyymmdd_topic/)
    └── research/          # 調査系の成果物(yyyymmdd_topic/)
```

### 命名と整理の方針

- スキルは .claude/skills/スキル名/SKILL.md の形が必須で、
  エージェントも .claude/agents/ 直下に置く。
  フォルダでのカテゴリ分けはせず、名前と「3. AIエージェント」の一覧で整理する。
- 新規のエージェント・スキルには、カテゴリ接頭辞を付ける
  (例:research-collector)。
  既存の realist / idealist / critic は、参照が壊れないため変更しない。
- 成果物は outputs/カテゴリ/yyyymmdd_topic/topic_summary.md に出力する。

## 3. AIエージェント

議論系
- realist(現実主義者):実現可能性、費用対効果、リスク
- idealist(理想主義者):創造性、可能性、長期的な価値
- critic(批判・検証担当):前提条件、反証、見落とし

調査系
- research-collector(情報収集担当):情報源の信頼性、新しさ、網羅性
- research-checker(裏取り担当):出典の確認、整合性、事実と推測の区別

各エージェントの詳細は「.claude/agents/」内の
Markdownファイルで定義する。

## 4. スキル

### setup-ai-team

AI組織の構築、エージェントの追加、
役割や指示の改善を支援する。

### multi-perspective

議論系の3エージェント(realist / idealist / critic)に
独立した分析を依頼し、意見の比較と最終結論の作成を行う。
調査系エージェントは呼び出さない。

## 5. 基本的な使い方

Claude Codeを本リポジトリのルートで起動する。
start-claude.bat（Windows）または start-claude.command（Mac）を
ダブルクリックでも起動できる。
Macで初回に動かない場合は、chmod +x start-claude.command を実行する。

- /multi-perspective：複数の視点から課題を分析する
- /setup-ai-team：AI組織の構築・改善を支援する

必要に応じて、スキルに議題や追加条件を指定する。

※ 実際の動作には、Claude Codeによる
エージェントの呼び出しが必要。

## 6. 運用方針

- 役割ごとの責任範囲を明確にする
- 既存の設定を確認してから変更する
- 大きな変更はGitのブランチで管理する
- 動作確認後に変更を取り込む
- 機能を増やしすぎず、必要性に応じて拡張する

## 7. 今後の拡張候補

- 技術アドバイザー
- 長期計画・戦略担当
- ファイルや成果物のレビュー担当
- エージェント間の連携方法の改善

## 8. 改善履歴

AI組織の役割、判断基準、運用方法を変更した際は、
変更内容とその理由を記録する。
