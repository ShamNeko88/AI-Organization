# 改善履歴

AI組織の役割、判断基準、運用方法を変更した際は、変更内容とその理由を記録する。

## 2026-11-19

作業ログの保存形式を .md から .txt に変更

- 内容：保存先を logs/yyyymmdd_workLog.txt にした（CLAUDE.md、docs/worklog.md を更新）。
- 理由：記録は1行のテキストで、Markdownの記法を使わないため。拡張子と中身を一致させ、Windowsでメモ帳などで開けるようにするため。
- 補足：config/worklog.json の `True` を `true` に修正（JSONとして正しくなるように）。

作業ログの設定ファイル化

- 内容：依頼ごとの作業ログを、config/worklog.json の `work_log_enabled` で設定できるようにした。
  詳細は docs/worklog.md。CLAUDE.md（6.作業ログ）、README、docs/setup.md から参照する。
- 理由：ログの記録を人間が設定ファイルで切り替えられるようにするため。
  フラグファイルより、設定の意味と場所が分かりやすいため。

配布準備

- 内容：LICENSE（MIT）と docs/setup.md（前提条件、言語、モデル設定、共通ルールの注意）を追加し、
  README に前提の一行と docs/setup.md への案内を追記した。
- 理由：他人に配布できる形にするため。READMEは短く保ち、詳細は docs/ に置いた。

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

research-it-news の調整（初回実行を受けて）

- 内容：項目数の上限（仮20件）、裏取りの深さの段階化（上位は一次情報まで、下位は出典・日付まで）、
  全情報源の取得結果の報告、curl での再試行、相手サーバーへの配慮（連続・並列アクセスの抑制、
  robots.txt と利用規約の確認）を SKILL.md と skills.md に追記した。
- 理由：初回実行で、エージェント合計が約30万トークン・約10分かかり、
  一部の情報源（JavaScript 描画、アクセス拒否）が取得できなかったため。
  取得できなかった情報源を「更新なし」と誤解しないようにする狙いもある。
- 補足：RSS や API の情報源は、実在確認と利用者の確定がまだのため、リストには追加していない。

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
