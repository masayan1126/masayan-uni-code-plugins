---
name: creating-profile-images
description: Generates Nano Banana Pro prompts for profile icons and SNS images. Use when user mentions "プロフィール画像", "アイコン作成", "SNS用画像", or "ヘッダー画像".
---

# プロフィール・SNS用画像作成

## ワークフロー

1. **用途確認**:
   - プロフィールアイコン: 400x400
   - Xヘッダー: 1500x500
   - X投稿用: 1200x675
2. **スタイル選択**:
   - イラスト風
   - フラットデザイン
   - 3D風
   - 手書き風
3. **要素ヒアリング**: モチーフ、カラー、雰囲気
4. **プロンプト生成**: PROMPT_TEMPLATE.md 使用
5. **成果物保存**:
   - プロンプト: `outputs/profile-sns/{タイトル}.md`
   - 生成画像: `outputs/profile-sns/images/{タイトル}.png`
6. **進捗更新**: profile-requests.md

## 参照ファイル

- [FORMATS.md](FORMATS.md): フォーマット定義
- [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md): テンプレート
- [EXAMPLES.md](EXAMPLES.md): サンプル

## 必須ルール

- 用途に応じたサイズ考慮
- 小さくても認識できるデザイン（アイコン）
