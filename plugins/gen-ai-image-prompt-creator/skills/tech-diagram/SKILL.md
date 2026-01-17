---
name: creating-tech-diagrams
description: Generates Nano Banana Pro prompts for technical explanation infographics. Use when user mentions "図解作成", "テック図解", or "AI解説図".
---

# テック・AI解説用図解作成

> **注**: 生成したプロンプトを画像生成AIに入力する際は、キャラクターの元画像を一緒に添付してください（解説役として配置）。

## ワークフロー

1. **アイデア確認**: `progress/ideas.md` をチェックし、該当するアイデアがあれば提案
2. **トピック確認**: 新規入力 or アイデアリストから選択
3. **画像テイスト確認**: ユーザーに以下から選択してもらう
   - **クリーン**: 整った線、モダンなインフォグラフィック風
   - **手書き風**: ラフスケッチ、走り書き風、親しみやすい雰囲気
4. **図解タイプ選択**:
   - フローチャート型: プロセス説明
   - 比較表型: 技術比較
   - 概念図型: 抽象概念
   - アーキテクチャ図型: システム構成
   - タイムライン型: 歴史・進化
5. **構成要素設計**: 3-5個のメイン要素に絞る
6. **AIっぽさ緩和オプション確認**: [ANTI_AI_STYLE.md](../ANTI_AI_STYLE.md) 参照
   - 図解系は「ベタ塗り」のみ推奨
7. **プロンプト生成**: PROMPT_TEMPLATE.md 使用（選択したテイストを反映）
8. **Xポスト文面生成**
9. **成果物保存**:
   - プロンプト: `output/tech-diagram/{タイトル}.md`（ディレクトリがなければ作成）
   - 生成画像: `output/tech-diagram/images/{タイトル}.png`
10. **進捗更新**: `progress/ideas.md` を更新（完了したアイデアにチェック）

## 参照ファイル

- [STYLES.md](STYLES.md): スタイル定義
- [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md): テンプレート
- [EXAMPLES.md](EXAMPLES.md): サンプル

## 必須ルール

- テキストは日本語
- 画像上部にタイトル配置
- 画像テイストは必ずユーザーに確認してからプロンプト生成
