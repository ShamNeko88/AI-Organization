# 作業ログ

## 概要

依頼が完了するたびに、作業内容を1行ずつ記録する機能。

## 設定

設定ファイル: `config/worklog.json`（Git管理対象）

```json
{
  "work_log_enabled": false
}
```

- `"work_log_enabled": false`：記録しない
- `"work_log_enabled": true`：依頼完了ごとに記録する

切り替えは、このファイルの値を書き換えるだけでよい。

## 記録先と形式

- 保存先：`logs/yyyymmdd_workLog.txt`（日付ごとに1ファイル。`logs/` はGit管理外）
- 形式：`yyyy-mm-dd HH:MM 概要(40文字程度)`
- ファイルや日付フォルダがなければ作成する
- 質問への回答のみの場合も記録対象

## Claudeの動作

- 依頼完了時に `config/worklog.json` を読み、`"work_log_enabled"` が `true` のときだけ追記する
- 追記したことは報告しない
- 設定の読み方はCLAUDE.md（6.作業ログ）に従う

## 注意

- Claudeは指示に従って設定を読むため、動作は確実ではない。確実に毎回記録したい場合は、Claude Codeの Stop フック（settings.json）を使う方法がある
