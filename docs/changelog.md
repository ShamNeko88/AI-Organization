# 改善履歴

AI組織の役割、判断基準、運用方法を変更した際は、変更内容とその理由を記録する。

## 2026-11-19

メンターの統合

- 内容：別リポジトリで運用していたメンターを統合した。
  メンターはエージェントではなく /mentor スキルとし、mentor-note / mentor-quiz /
  mentor-organizer / mentor-review を .claude/skills/ に移した。
  保存先は output/ から outputs/mentor/（notes / quiz / review）に変更した。
- 理由：本リポジトリを様々なエージェントをまとめる場所にするため。
  常時メンター化する設定（CLAUDE.md）は、司令塔のルールと干渉し、起動時の読み込みも増えるため、
  取り込まず、呼んだときだけ動くスキルにした。CLAUDE.md は共通ルールだけを保つ。
- 補足：/mentor は disable-model-invocation で手動呼び出し専用にした。
  outputs/mentor/ の中身は個人的な内容のためGit管理外とし、.gitkeep のみ管理する。
  旧CLAUDE.mdの「記録のルール」は、各スキルと /mentor に分けて移した。

research-it-news の追加

- 内容：IT・セキュリティニュースを、情報源リストから収集・裏取り・要約するスキルを追加した。
  既存の research-collector と research-checker を使い、新しいエージェントは作っていない。
  手動呼び出し専用で、期間とテーマを指定できる。
- 理由：ニュース収集を、毎回の検索任せにせず、同じ型で繰り返せるようにするため。
  情報源リストは暫定で、利用者の確認後に確定する。

モデル設定の変更

- 内容：research-checker と critic の model を inherit から opus に変更した。
  research-collector、realist、idealist は inherit のまま。
- 理由：裏取りと批判は、判断や検証の精度が重要なため。
- 補足：opus はモデルの別名。使えるモデルは環境で異なるため、変更方法は agents.md に記載した。

ドキュメントの整理

- 内容：README を目的・使い方・一覧・運用のコツ・docs/ への案内に絞り、
  詳細を docs/（agents / skills / mentor / changelog）に移した。
  旧 README の内容（フォルダ構成、命名方針、運用方針、拡張候補）は agents.md に移した。
- 理由：README を短く保ち、詳細を必要なときだけ読めるようにするため。
