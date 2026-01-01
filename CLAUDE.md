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
└── SKILL.md
```
