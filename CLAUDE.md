# CLAUDE.md - masayan-uni-plugins

## プラグイン追加時の必須作業

新しいスキルをプラグインとして追加する際は、以下の2つのファイルを必ず更新すること：

### 1. `.claude-plugin/marketplace.json`

`plugins`配列に新しいプラグインのエントリを追加：

```json
{
  "name": "プラグイン名",
  "description": "説明",
  "version": "1.0.0",
  "author": { "name": "masayan" },
  "source": "./plugins/プラグイン名",
  "category": "development"
}
```

### 2. `README.md`（ルート）

「Available Plugins」テーブルに新しいプラグインの行を追加：

```markdown
| [プラグイン名](./plugins/プラグイン名) | 説明 | バージョン |
```

## プラグインの構造

各プラグインは `plugins/` ディレクトリ配下に作成し、最低限以下の構成とする：

```
plugins/プラグイン名/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── 動詞-対象.md
└── skills/
    └── スキル名/
        └── SKILL.md
```

## スキルとコマンドのセット

スキルを追加する際は、必ず対応するコマンドファイルも作成すること。

### 1. plugin.json に commands ディレクトリを指定

```json
{
  "commands": "./commands/"
}
```

### 2. commands/ ディレクトリにコマンドファイルを作成

ファイル名がスラッシュコマンド名になる（例: `fetch-ai-news.md` → `/fetch-ai-news`）

```markdown
---
description: コマンドの説明
---

Execute the skill at `skills/スキル名` to ...
```

**コマンド名のルール：**
- 動詞で開始する（例: `create-`, `generate-`, `fetch-`, `scan-`, `convert-`, `extract-`）
- ケバブケース（小文字とハイフン）を使用
