---
name: creating-engineer-manga
description: Generates Nano Banana Pro prompts for 4-panel engineer humor comics. Use when user mentions "漫画作成", "エンジニア漫画", "4コマ", or "あるある". Requires character image attachment when using generated prompts.
---

# エンジニアあるある漫画作成

> **重要**: 生成したプロンプトを画像AIに入力する際は、キャラクターの元画像を添付すること。

## ワークフロー

1. **テーマ確認**: progress/manga-ideas.md のネタストックから選択 or 新規入力
2. **パターン選択**（対話形式で確認）:
   - 日常系4コマ（デフォルト）: 起承転結、ほのぼの
   - バトル系縦スクロール: 4-6コマ、ダイナミック
   - キャラ固定ギャグ: 2-4コマ、表情重視
3. **プロンプト生成**: PROMPT_TEMPLATE.md 使用
4. **Xポスト文面生成**: ハッシュタグ付き
5. **成果物保存**:
   - プロンプト: `outputs/engineer-manga/{タイトル}.md`
   - 生成画像: `outputs/engineer-manga/images/{タイトル}.png`
6. **進捗更新**: manga-ideas.md を更新

## 参照ファイル

- [PATTERNS.md](PATTERNS.md): パターン定義
- [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md): テンプレート
- [EXAMPLES.md](EXAMPLES.md): サンプル

## 必須ルール

- テキストは日本語
- 画像上部にタイトル配置
- 手書き風テイスト
- エンジニアに共感されるユーモア

## 長編制作時の注意

複数ページの漫画を制作する場合：

- **1ページずつ生成**: 一度に多くのページを生成しない（一貫性が崩壊しやすい）
- **参照画像の再添付**: 各生成ごとにキャラクター設定画を必ず再添付
- **品質の細かな確認**: 小さな単位で生成し、各ページの品質を高く保つ
