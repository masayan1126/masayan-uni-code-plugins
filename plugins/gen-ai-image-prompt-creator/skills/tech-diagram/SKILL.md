---
name: creating-tech-diagrams
description: Generates Nano Banana Pro prompts for technical explanation infographics. Use when user mentions "図解作成", "テック図解", or "AI解説図". Requires character image attachment for narrator placement.
---

# テック・AI解説用図解作成

> **重要**: 生成したプロンプトを画像AIに入力する際は、キャラクターの元画像を添付すること（解説役として配置）。

## ワークフロー

1. **トピック確認**: progress/diagram-topics.md から選択 or 新規入力
2. **画像テイスト確認**: ユーザーに以下から選択してもらう
   - **クリーン**: 整った線、モダンなインフォグラフィック風
   - **手書き風**: ラフスケッチ、走り書き風、親しみやすい雰囲気
3. **図解タイプ選択**:
   - フローチャート型: プロセス説明
   - 比較表型: 技術比較
   - 概念図型: 抽象概念
   - アーキテクチャ図型: システム構成
   - タイムライン型: 歴史・進化
4. **構成要素設計**: 3-5個のメイン要素に絞る
5. **プロンプト生成**: PROMPT_TEMPLATE.md 使用（選択したテイストを反映）
6. **Xポスト文面生成**
7. **成果物保存**:
   - プロンプト: `outputs/tech-diagram/{タイトル}.md`
   - 生成画像: `outputs/tech-diagram/images/{タイトル}.png`
8. **進捗更新**

## 参照ファイル

- [STYLES.md](STYLES.md): スタイル定義
- [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md): テンプレート
- [EXAMPLES.md](EXAMPLES.md): サンプル

## 必須ルール

- テキストは日本語
- 画像上部にタイトル配置
- 画像テイストは必ずユーザーに確認してからプロンプト生成
