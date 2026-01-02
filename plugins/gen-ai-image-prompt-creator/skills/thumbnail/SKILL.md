---
name: creating-thumbnails
description: Generates Nano Banana Pro prompts for blog and YouTube thumbnail images. Use when user mentions "サムネイル作成", "サムネ", "YouTube用画像", or "ブログ画像".
---

# サムネイル画像作成

## ワークフロー

1. **プラットフォーム確認**:
   - ブログ: 1200x630 (OGP)
   - YouTube: 1280x720 (16:9)
2. **コンテンツ確認**: タイトル（20文字以内推奨）、テーマ
3. **スタイル選択**:
   - テキスト中心型
   - 人物・キャラ型（※キャラ画像添付前提）
   - コンセプト型
   - 比較型
4. **キャラクター確認**（人物・キャラ型の場合）:
   - 既存キャラクター使用 → ベース画像の添付が必要な旨を明記
   - 新規キャラクター → キャラクター詳細をプロンプトに記載
5. **プロンプト生成**: PROMPT_TEMPLATE.md 使用
6. **成果物保存**:
   - プロンプト: `outputs/thumbnail/{タイトル}.md`
   - 生成画像: `outputs/thumbnail/images/{タイトル}.png`
7. **進捗更新**: thumbnail-queue.md

## 参照ファイル

- [FORMATS.md](FORMATS.md): フォーマット定義
- [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md): テンプレート
- [EXAMPLES.md](EXAMPLES.md): サンプル

## 必須ルール

- 日本語テキスト
- 高コントラスト配色
- クリック率を意識したデザイン
