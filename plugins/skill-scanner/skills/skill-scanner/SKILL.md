---
name: skill-scanner
description: Macで登録済みClaude agent skillsをスキャンし一覧表示。「スキルを調べて」「登録済みスキル一覧」などで使用。読み取り専用で安全に実行。
---

# Skill Scanner

登録されているClaude agent skillsをスキャンし一覧表示する（読み取り専用）。

## 使用方法

詳細は `scripts/scan_skills.py --help` を参照。

```bash
# 基本スキャン（ユーザーレベルのみ）
python3 scripts/scan_skills.py

# ~/git以下のプロジェクトもスキャン（要ユーザー確認）
python3 scripts/scan_skills.py --git-projects

# JSON形式で出力
python3 scripts/scan_skills.py --json
```

**重要**: `~/git`以下をスキャンする際は必ずユーザーに確認してから実行。
