# skill-scanner

Scan and list registered Claude agent skills on Mac. Read-only, safe operation.

## Features

- Scans user-level skills (`~/.claude/skills/`)
- Optionally scans project-level skills (`~/git/**/.claude/skills/`)
- Supports monorepo structures (up to 3 levels deep)
- JSON output for programmatic use

## Installation

```bash
/plugin marketplace add masayan/masayan-uni-code-plugins
/plugin install skill-scanner@masayan-uni-plugins
```

## Usage

Invoke the skill in Claude Code:

```
/skill-scanner
```

Or ask naturally:
- "スキルを調べて"
- "登録済みスキル一覧"

## Skill Files

- `SKILL.md` - Main skill definition
- `scripts/scan_skills.py` - Python script for scanning

## License

MIT
