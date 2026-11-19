# エージェント

各エージェントは .claude/agents/ のMarkdownファイルで定義する。
役割と判断基準の詳細は、各ファイルを参照する。

## 議論系

- realist（現実主義者）：実現可能性、費用対効果、リスクを重視する。
  判断基準の順は、実現可能性、費用対効果、失敗時のリスク、短期成果、中長期利益。
- idealist（理想主義者）：創造性、可能性、長期的な価値を重視する。
- critic（批判・検証担当）：前提条件、反証、見落としを指摘する。重箱の隅も指摘するが、
  目的はリスクや見落としの指摘であり、指摘そのものではない。

## 調査系

- research-collector（情報収集担当）：情報源の信頼性、新しさ、網羅性を重視し、出典付きで整理する。
  意見や結論は述べず、材料を揃える。
- research-checker（裏取り担当）：出典の確認、整合性、事実と推測の区別を行う。
  確認結果は「確認済み / 一部確認 / 未確認 / 矛盾あり」で示す。収集は行わない。

## メンター

メンターはエージェントではなくスキル（/mentor）として持つ。常時有効にせず、呼んだときだけ動く。
詳細は [mentor.md](mentor.md) を参照。

## モデル設定

frontmatter の model で、エージェントごとに使うモデルを指定できる。

- inherit：使用中のモデルを引き継ぐ（既定）
- opus / sonnet / haiku：モデルの別名（エイリアス）。環境で現在対応するモデルが使われる
- モデルIDの直接指定も可能

現在の設定

- research-checker：opus（出典・日付・整合性の検証精度が重要なため）
- critic：opus（見落としや前提の弱さを見つける判断精度が重要なため）
- research-collector、realist、idealist：inherit（既定のまま）

変更方法

1. .claude/agents/<エージェント名>.md の frontmatter の model を書き換える。
2. 使えるモデルは環境（契約・組織の設定）で異なる。Claude Codeの /model で選べるものを確認し、
   使えない場合は inherit に戻すか、使えるモデルの別名またはIDに変更する。

注意：エイリアスの opus が実際にどのモデルを指すかは環境で変わる。
本リポジトリでは、環境ごとの具体的なモデル名を固定しない。

## フォルダ構成

```text
AI-Organization/
├── README.md
├── CLAUDE.md              # 共通ルール
├── start-claude.bat       # Windows用の起動ファイル
├── start-claude.command   # Mac用の起動ファイル
├── docs/                  # 詳細ドキュメント
├── .claude/
│   ├── agents/            # エージェント（realist, idealist, critic, research-collector, research-checker）
│   └── skills/            # スキル（スキル名/SKILL.md）
└── outputs/
    ├── discussion/        # 議論系の成果物（yyyymmdd_topic/）
    ├── research/          # 調査系の成果物（yyyymmdd_topic/）
    └── mentor/            # メンターの記録（notes / quiz / review）。Git管理外
```

## 命名と整理の方針

- スキルは .claude/skills/スキル名/SKILL.md の形が必須で、エージェントも .claude/agents/ 直下に置く。
  フォルダでのカテゴリ分けはせず、名前と一覧で整理する。
- 新規のエージェント・スキルには、カテゴリ接頭辞を付ける（例：research-collector、mentor-note）。
  既存の realist / idealist / critic は、参照が壊れないため変更しない。
- 成果物は outputs/カテゴリ/yyyymmdd_topic/topic_summary.md に出力する。
  メンターの記録は outputs/mentor/ 配下に、各スキルが定める形式で保存する。

## 運用方針

- 役割ごとの責任範囲を明確にする。
- 既存の設定を確認してから変更する。
- 大きな変更はGitのブランチで管理する。
- 動作確認後に変更を取り込む。
- 機能を増やしすぎず、必要性に応じて拡張する。
- エージェントやスキルを追加したら、README の一覧と docs/ を更新する。
- 役割、判断基準、運用方法を変更したら、変更内容と理由を [changelog.md](changelog.md) に記録する。

## 今後の拡張候補

- 技術アドバイザー
- 長期計画・戦略担当
- ファイルや成果物のレビュー担当
- エージェント間の連携方法の改善
