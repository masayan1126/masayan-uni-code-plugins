---
name: technyan-x-post-generator
description: 記事からテクにゃん.のXアカウント用ポスト投稿案を生成。日英両方の投稿案を3パターンずつ生成。
---

# X Post Generator Skill

記事のパスを指定して、テクにゃん.のXアカウント用のポスト投稿案を生成するスキル。

## 使い方

```
/x-post src/content/articles/YYYYMMDD/article-slug/ja.md
```

## 出力

- 日本語版 3パターン
- 英語版 3パターン
- 記事URL、ハッシュタグ、OGP画像添付指示を含む

## 参照ドキュメント

- [WORKFLOW.md](./WORKFLOW.md) - 実行手順
- [TEMPLATES.md](./TEMPLATES.md) - ポストテンプレート
- [HASHTAG_MAP.md](./HASHTAG_MAP.md) - ハッシュタグ変換ルール
- [EXAMPLES.md](./EXAMPLES.md) - 出力例
