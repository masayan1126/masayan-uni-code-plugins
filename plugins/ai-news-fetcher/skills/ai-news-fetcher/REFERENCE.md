# AI News Fetcher Reference

## MCP Tools Used

### Tavily Search
**Tool**: `mcp__tavily-mcp__tavily-search`

**Parameters**:
```json
{
  "query": "latest AI artificial intelligence news developments updates",
  "topic": "news",
  "time_range": "day",
  "max_results": 30,
  "search_depth": "advanced",
  "include_raw_content": true
}
```

## File Paths

### Content Directory
```
src/content/articles/{YYYYMMDD}/
```

### Schema Configuration
```
src/content/config.ts
```

## Schema Structure

### Article Frontmatter
```typescript
{
  title: string,           // Article title
  description: string,     // Brief description (100-150 chars)
  date: Date,             // ISO format YYYY-MM-DD
  category: 'ChatGPT' | 'Claude' | 'Image Generation' | 'Research' | 'Other',
  locale: 'en' | 'ja',    // Language
  tags: string[]          // Optional array of tags
}
```

## Existing Categories

- **ChatGPT**: OpenAI, GPT models, ChatGPT features
- **Claude**: Anthropic, Claude models, AI safety
- **Image Generation**: Stable Diffusion, Midjourney, DALL-E
- **Research**: Academic papers, research breakthroughs
- **Other**: General AI news, industry updates

## Duplicate Detection

### Process
1. Read all existing `.md` files in `src/content/articles/`
2. Extract `title` from frontmatter
3. Compare with new article titles using fuzzy matching
4. Similarity threshold: 80%+
5. Skip articles that match existing titles

### Fuzzy Match Algorithm
- Lowercase both titles
- Remove common words (the, a, an, etc.)
- Calculate Levenshtein distance or token overlap
- Consider duplicates if similarity > 80%

## Category Auto-Detection

### Keywords Mapping
```
ChatGPT: [openai, gpt, chatgpt, gpt-4, gpt-5]
Claude: [anthropic, claude, constitutional ai]
Image Generation: [stable diffusion, midjourney, dall-e, dalle, image synthesis, text-to-image, imagen]
Research: [paper, study, research, breakthrough, academic, arxiv, conference]
Other: [default for unmatched]
```

### New Category Detection
If content doesn't match existing categories (confidence < 50%):
1. Suggest new category name based on topic
2. Update `src/content/config.ts` with new category
3. Add keyword mapping for future detection

## File Naming Convention

### Slug Generation
- Extract main topic from title
- Convert to lowercase
- Replace spaces with hyphens
- Remove special characters
- Max length: 60 characters

### Examples
```
"OpenAI Announces GPT-5" → openai-announces-gpt5
"Claude 3.5 Sonnet Released" → claude-35-sonnet-released
"Stable Diffusion 3 Turbo" → stable-diffusion-3-turbo
```

### File Naming
```
{slug}.md        # English version
{slug}-ja.md     # Japanese version
```

## Tag Generation

### Guidelines
- 3-5 tags per article
- Include:
  - Company names (OpenAI, Anthropic, etc.)
  - Technology names (GPT-4, Claude, etc.)
  - Key concepts (AI Safety, Code Generation, etc.)
  - Application domains (Healthcare, Education, etc.)

### Format
```
tags: ["OpenAI", "GPT-5", "Large Language Models"]
```

## Content Quality Checklist

- [ ] Title is clear and descriptive
- [ ] Description is concise (100-150 chars)
- [ ] Date is in YYYY-MM-DD format
- [ ] Category is correctly assigned
- [ ] Tags are relevant and properly formatted
- [ ] Content is 300-600 words
- [ ] Headings use proper markdown (##, ###)
- [ ] Facts are accurate and verifiable
- [ ] No speculation or opinion
- [ ] Both EN and JA versions created
- [ ] Files saved in correct directory

## Error Handling

### No News Found
- Report: "No new AI news found in the past 24 hours"
- Do not create any files

### All Articles are Duplicates
- Report: "All fetched articles are duplicates of existing content"
- List duplicate titles

### API Errors
- Report Tavily MCP error message
- Do not create partial content

### Schema Update Failure
- Create articles with existing categories only
- Report which articles couldn't be categorized
- Suggest manual category addition

## Usage Example

```bash
# In Claude Code CLI
/ai-news-fetcher
```

Expected output:
```
Fetching latest AI news...
Found 30 articles from Tavily
Checking for duplicates...
Filtered to 12 unique articles
Generating English content...
Generating Japanese content...
Created 24 files in src/content/articles/20251118/

Summary:
- Total fetched: 30
- Unique articles: 12
- Files created: 24 (12 EN + 12 JA)
- New categories: 0
- Duplicates skipped: 18

Files created:
- openai-gpt5-preview.md
- openai-gpt5-preview-ja.md
- anthropic-claude-update.md
- anthropic-claude-update-ja.md
...
```
