---
name: creating-thumbnails
description: Generates Nano Banana Pro prompts for blog and YouTube thumbnail images. Use when user mentions "サムネイル作成", "サムネ", "YouTube用画像", or "ブログ画像".
---

# サムネイル画像作成

## ワークフロー

1. **アイデア確認**: `progress/ideas.md` をチェックし、該当するアイデアがあれば提案
2. **プラットフォーム確認**:
   - ブログ: 1200x630 (OGP)
   - YouTube: 1280x720 (16:9)
3. **コンテンツ確認**: タイトル（20文字以内推奨）、テーマ
4. **スタイル選択**:
   - テキスト中心型
   - 人物・キャラ型（※キャラ画像添付前提）
   - コンセプト型
   - 比較型
5. **キャラクター確認**（人物・キャラ型の場合）:
   - 既存キャラクター使用 → ベース画像の添付が必要な旨を明記
   - 新規キャラクター → キャラクター詳細をプロンプトに記載
6. **プロンプト生成**: PROMPT_TEMPLATE.md 使用
7. **成果物保存**:
   - プロンプト: `output/thumbnail/{タイトル}.md`（ディレクトリがなければ作成）
   - 生成画像: `output/thumbnail/images/{タイトル}.png`
8. **進捗更新**: `progress/ideas.md` を更新（完了したアイデアにチェック）

## 参照ファイル

- [FORMATS.md](FORMATS.md): フォーマット定義
- [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md): テンプレート
- [EXAMPLES.md](EXAMPLES.md): サンプル

## 必須ルール

- 日本語テキスト
- 高コントラスト配色
- クリック率を意識したデザイン
