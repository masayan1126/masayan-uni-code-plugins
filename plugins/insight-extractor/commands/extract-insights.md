---
description: URLまたは文章から価値のあるインサイト（体験談・専門知識・ベストプラクティス）を抽出
---

Execute the skill at `~/.claude/plugins/insight-extractor/skills/insight-extractor` to extract valuable insights from the provided URL or text.

If a URL is provided, use WebFetch to retrieve the content first.
If text is provided directly, analyze it immediately.

Follow the extraction rules in EXTRACTION_RULES.md to identify and summarize insights with their locations.
