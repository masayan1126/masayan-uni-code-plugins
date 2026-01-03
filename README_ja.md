# masayan-uni-plugins

ドキュメント作成・開発ワークフロー向けのClaude Codeプラグイン集。

## 利用可能なプラグイン

| プラグイン | 説明 | バージョン |
|-----------|------|-----------|
| [claude-md-creator](./plugins/claude-md-creator) | WHY/WHAT/HOW構造で最適なCLAUDE.mdを作成 | 1.0.0 |
| [skill-scanner](./plugins/skill-scanner) | Mac上の登録済みClaude agentスキルをスキャン・一覧表示 | 1.0.0 |
| [image-converter](./plugins/image-converter) | PNG/JPG/JPEG画像をWebP、ICO、SVG形式に変換 | 1.0.0 |
| [ocr](./plugins/ocr) | OCRで画像からテキストを抽出しクリップボードにコピー | 1.0.0 |
| [gen-ai-image-prompt-creator](./plugins/gen-ai-image-prompt-creator) | イラスト、キャラクター、漫画、サムネイル、図解、SNS向け画像プロンプト生成 | 1.0.0 |
| [ai-news-fetcher](./plugins/ai-news-fetcher) | AIニュースを取得し日英バイリンガル記事を生成 | 1.0.0 |
| [technyan-x-post-generator](./plugins/technyan-x-post-generator) | テックにゃんキャラクターのXポスト下書き生成 | 1.0.0 |
| [note-optimizer](./plugins/note-optimizer) | noteプラットフォーム向けに記事を最適化 | 1.0.0 |
| [x-post-optimizer](./plugins/x-post-optimizer) | アルゴリズムとエンゲージメント向けにXポストを最適化 | 1.0.0 |
| [youtube-metadata-creator](./plugins/youtube-metadata-creator) | テック動画向けYouTubeメタデータ生成 | 1.0.0 |
| [tech-blog-writer](./plugins/tech-blog-writer) | SEO対策済みテックブログ記事の作成・最適化 | 1.0.0 |
| [chrome-ext-toolkit](./plugins/chrome-ext-toolkit) | Chrome拡張機能の開発とレビュー対応 | 1.0.0 |
| [bgm-creator](./plugins/bgm-creator) | Suno BGMプロンプト生成とYouTubeアップロード | 1.0.0 |

## 未プラグイン化スキル（プロジェクト固有）

以下のスキルは特定プロジェクトに強く依存するため、プラグイン化していません。

| プロジェクト | スキル | 説明 |
|-------------|-------|------|
| masayan-tech-blog | tech-blog-frontend-optimizer | テックブログのフロントエンド改善（PV・滞在時間向上、SEO最適化） |
| claude-code-forest | Blog Publisher Skill | ブログ記事作成とNILTO CMSへの自動入稿 |

## インストール

### マーケットプレイスの追加

```bash
/plugin marketplace add masayan/masayan-uni-code-plugins
```

### プラグインのインストール

```bash
/plugin install claude-md-creator@masayan-uni-plugins
```

## ライセンス

MIT
