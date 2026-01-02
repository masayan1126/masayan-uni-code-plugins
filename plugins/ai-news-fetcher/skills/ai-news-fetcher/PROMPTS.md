# Content Generation Prompts

## English Article Template

```markdown
---
title: "{Article Title}"
description: "{Brief 1-2 sentence description}"
date: {YYYY-MM-DD}
category: "{Category}"
locale: "en"
tags: [{list of relevant tags}]
---

# {Article Title}

{Opening paragraph with key information}

## {Section 1 Title}

{Content for section 1}

### {Subsection if needed}

{Subsection content}

## {Section 2 Title}

{Content for section 2}

## {Additional sections as needed}

{Wrap up with implications or next steps}

## Sources

- [Source Title 1](https://example.com/source1)
- [Source Title 2](https://example.com/source2)
```

## Japanese Article Template

```markdown
---
title: "{日本語タイトル}"
description: "{簡潔な1-2文の説明}"
date: {YYYY-MM-DD}
category: "{Category}"
locale: "ja"
tags: [{関連タグのリスト}]
---

# {日本語タイトル}

{重要な情報を含む冒頭段落}

## {セクション1のタイトル}

{セクション1の内容}

### {必要に応じてサブセクション}

{サブセクションの内容}

## {セクション2のタイトル}

{セクション2の内容}

## {必要に応じて追加セクション}

{影響や次のステップでまとめる}

## 情報源

- [ソースタイトル1](https://example.com/source1)
- [ソースタイトル2](https://example.com/source2)
```

## Article Generation Guidelines

### Title Guidelines
- **English**: Clear, descriptive, newsworthy (50-80 characters)
- **Japanese**: Natural Japanese phrasing, informative (20-40 characters)

### Description Guidelines
- **English**: 1-2 sentences, 100-150 characters
- **Japanese**: 1-2 sentences, 50-80 characters
- Include key value proposition or main point

### Content Structure
1. **Opening paragraph**: Who, what, when, why - answer immediately
2. **Main sections**: 2-4 major sections with clear headings
3. **Use subsections**: Break down complex information
4. **Bullet points**: For lists and key features
5. **Closing**: Implications, availability, or next steps

### Tone and Style
- **Professional yet accessible**: Technical accuracy without jargon overload
- **Informative**: Focus on facts and insights
- **Neutral**: Objective reporting, avoid hype
- **Concise**: 300-600 words per article

### Category Assignment Logic

**ChatGPT**
- Keywords: OpenAI, GPT-4, GPT-5, ChatGPT, GPT models
- Topics: ChatGPT features, plugins, enterprise

**Claude**
- Keywords: Anthropic, Claude, Constitutional AI
- Topics: Claude models, safety features, API updates

**Image Generation**
- Keywords: Stable Diffusion, Midjourney, DALL-E, image synthesis, text-to-image
- Topics: Image models, generative art, visual AI

**Research**
- Keywords: paper, study, research, breakthrough, academic
- Topics: New techniques, scientific findings, benchmarks

**Other**
- Everything else: Industry news, regulations, acquisitions, general AI updates

### Tag Generation
- Generate 3-5 relevant tags per article
- Use proper capitalization (e.g., "OpenAI", "AI Safety")
- Include:
  - Company/organization names
  - Technology names
  - Key concepts
  - Application domains

### Slug Generation
- Lowercase with hyphens
- Based on main topic/headline
- Keep under 60 characters
- Examples:
  - "openai-gpt5-announcement"
  - "anthropic-claude-safety-update"
  - "stable-diffusion-3-turbo"

### Translation Guidelines (EN → JA)
- **Not literal translation**: Adapt for Japanese readers
- **Natural Japanese**: Use appropriate formality (です・ます調)
- **Technical terms**: Use established Japanese terms where available
- **Structure**: May reorganize for Japanese readability
- **Length**: Japanese version may be 60-80% of English word count

### Quality Standards
- Fact-check against source material
- Include specific details (version numbers, dates, metrics)
- Cite company/source when relevant
- Avoid speculation - stick to announced facts
- Proofread for grammar and clarity
