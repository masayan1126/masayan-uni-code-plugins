# masayan-uni-plugins

Claude Code plugins for documentation and development workflows.

## Available Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| [claude-md-creator](./plugins/claude-md-creator) | Create optimal CLAUDE.md files with WHY/WHAT/HOW structure | 1.0.0 |
| [skill-scanner](./plugins/skill-scanner) | Scan and list registered Claude agent skills on Mac | 1.0.0 |
| [image-converter](./plugins/image-converter) | Convert PNG/JPG/JPEG images to WebP, ICO, SVG formats | 1.0.0 |
| [ocr](./plugins/ocr) | Extract text from images using OCR and copy to clipboard | 1.0.0 |
| [gen-ai-image-prompt-creator](./plugins/gen-ai-image-prompt-creator) | Generate image prompts for illustrations, characters, manga, thumbnails, diagrams, and SNS | 1.0.0 |
| [ai-news-fetcher](./plugins/ai-news-fetcher) | Fetch AI news and generate bilingual markdown articles | 1.0.0 |
| [technyan-x-post-generator](./plugins/technyan-x-post-generator) | Generate X post drafts for Tech-nyan character | 1.0.0 |
| [note-optimizer](./plugins/note-optimizer) | Optimize articles for note platform | 1.0.0 |
| [x-post-optimizer](./plugins/x-post-optimizer) | Optimize X posts for algorithm and engagement | 1.0.0 |
| [youtube-metadata-creator](./plugins/youtube-metadata-creator) | Generate YouTube video metadata for tech videos | 1.0.0 |
| [tech-blog-writer](./plugins/tech-blog-writer) | Create and optimize tech blog articles with SEO | 1.0.0 |
| [chrome-ext-toolkit](./plugins/chrome-ext-toolkit) | Chrome extension development and review response | 1.0.0 |
| [bgm-creator](./plugins/bgm-creator) | Generate Suno BGM prompts and upload to YouTube | 1.0.0 |

## Unplugged Skills (Project-Specific)

以下のスキルは特定プロジェクトに強く依存するため、プラグイン化していません。

| Project | Skill | Description |
|---------|-------|-------------|
| masayan-tech-blog | tech-blog-frontend-optimizer | テックブログのフロントエンド改善（PV・滞在時間向上、SEO最適化） |
| claude-code-forest | Blog Publisher Skill | ブログ記事作成とNILTO CMSへの自動入稿 |

## Installation

### Adding this Marketplace

```bash
/plugin marketplace add masayan/masayan-uni-code-plugins
```

### Installing Plugins

```bash
/plugin install claude-md-creator@masayan-uni-plugins
```

## License

MIT
