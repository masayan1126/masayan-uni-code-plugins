# AI News Fetcher Workflow

## Overview
This skill fetches the latest AI news using Tavily MCP and generates bilingual markdown articles organized by date.

## Execution Steps

### 1. Get Current Date
- Format: `YYYYMMDD` (e.g., `20251118`)
- Use this for directory name

### 2. Create Date Directory
- Path: `src/content/articles/{YYYYMMDD}/`
- Skip if already exists

### 3. Fetch Latest AI News via Tavily MCP
Use the `mcp__tavily-mcp__tavily-search` tool with parameters:
```
query: "latest AI artificial intelligence news developments updates"
topic: "news"
time_range: "day"
max_results: 30
search_depth: "advanced"
include_raw_content: true
```

### 4. Check for Duplicates
- Read all existing article files in `src/content/articles/`
- Extract titles from frontmatter
- Compare with fetched news titles (fuzzy match)
- Filter out duplicates

### 5. Categorize Each Article
Analyze content and assign category:
- **ChatGPT**: OpenAI, GPT models, ChatGPT features
- **Claude**: Anthropic, Claude models
- **Image Generation**: Stable Diffusion, Midjourney, DALL-E, image AI
- **Research**: Academic papers, research breakthroughs, new techniques
- **Other**: General AI news, industry updates, regulations

Auto-generate relevant tags (3-5 per article).

If content doesn't fit existing categories, suggest new category name.

### 6. Record Source URLs
**重要**: 記事作成時に参照したURLを必ず記録する
- 各記事に使用したソースURLをリスト化
- 記事末尾の「Sources」/「情報源」セクションに追加
- 複数ソースがある場合は全て記載

### 7. Generate Bilingual Markdown
For each article:
1. Create English version (`{slug}.md`)
2. Create Japanese version (`{slug}-ja.md`)
3. **必須**: 記事末尾に出典URLを追加

Use templates from [PROMPTS.md](./PROMPTS.md)

### 8. Update Schema if Needed
If new categories were created:
- Update `src/content/config.ts`
- Add new category to the enum

### 9. Save Files
Write all markdown files to:
```
src/content/articles/{YYYYMMDD}/{slug}.md
src/content/articles/{YYYYMMDD}/{slug}-ja.md
```

### 10. Summary Report
Provide summary:
- Total articles fetched
- Total articles created (after duplicate removal)
- New categories added (if any)
- File paths created
- **Source URLs used** (各記事の参照元URL一覧)
