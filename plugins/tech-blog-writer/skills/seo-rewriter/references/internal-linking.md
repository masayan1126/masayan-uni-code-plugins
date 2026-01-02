# 内部リンク戦略ガイド

サイト内の記事間を効果的につなぎ、SEOとユーザー体験を向上させる内部リンク戦略です。

## 内部リンクの重要性

### SEOへの効果

- **クロール促進**: クローラーが他ページを発見しやすくなる
- **リンクジュース分配**: ページランクが分散される
- **関連性シグナル**: トピッククラスターを形成
- **インデックス促進**: 新しいページが早くインデックスされる

### ユーザー体験の向上

- **回遊率向上**: 関連情報へ簡単にアクセス
- **滞在時間増加**: サイト内を長く閲覧
- **直帰率低下**: 他ページへの導線
- **学習効率**: 段階的な情報取得

## 内部リンクの種類

### 1. コンテキストリンク（文中リンク）

本文中の自然な文脈でのリンク:

```markdown
React Hooksの中でも、useStateは最も基本的で重要なフックです。
さらに詳しくは[useStateの使い方完全ガイド](./usestate-guide)をご覧ください。

useEffectと組み合わせることで、より複雑な処理も実現できます。
[useEffectの実践例](./useeffect-examples)も参考になります。
```

**ベストプラクティス:**
- 自然な文脈に配置
- アンカーテキストが説明的
- 1段落に1-2個まで
- 読み進める妨げにならない位置

### 2. 関連記事セクション

記事末尾の関連記事リスト:

```markdown
## 関連記事

本記事と合わせて読みたい記事:

### React Hooks シリーズ
- [useStateの使い方完全ガイド](./usestate-guide)
  - 状態管理の基本から実践パターンまで
- [useEffectマスターガイド](./useeffect-guide)
  - 副作用処理とクリーンアップの完全解説
- [カスタムフックの作り方](./custom-hooks)
  - 再利用可能なロジックの実装

### 次のステップ
- [React パフォーマンス最適化](./react-performance)
  - useMemo、useCallbackによる最適化
- [TypeScript + React開発](./typescript-react)
  - 型安全なReact開発のベストプラクティス
```

### 3. ナビゲーションリンク

目次や前後記事へのリンク:

```markdown
## 目次
1. [React Hooksとは？](#what-is-hooks)
2. [useStateの使い方](#usestate)
3. [useEffectの使い方](#useeffect)
4. [まとめ](#summary)

---

← [前の記事: React 基礎](./react-basics)
→ [次の記事: React Router](./react-router)
```

### 4. サイドバー・フッターリンク

サイト構造を示すリンク:

```markdown
### 人気記事
- React Hooks完全ガイド
- TypeScript入門
- Next.js チュートリアル

### カテゴリー
- React (25)
- TypeScript (18)
- Node.js (12)
```

## アンカーテキストの最適化

### 効果的なアンカーテキスト

```markdown
✅ 説明的でキーワードを含む
さらに詳しくは[useStateの使い方完全ガイド](./usestate-guide)をご覧ください。

✅ 自然な文章
[React Hooksの基本](./react-hooks-basics)を理解していれば、
カスタムフックの作成も簡単です。

❌ 曖昧
詳しくは[こちら](./usestate-guide)をクリック。

❌ 同じアンカーテキストの重複
[詳細](./page1)、[詳細](./page2)、[詳細](./page3)
```

### アンカーテキストのパターン

**記事タイトルそのまま:**
```markdown
[React Hooks完全ガイド｜useState/useEffectの使い方](./react-hooks-guide)
```

**要約版:**
```markdown
[React Hooksの基本](./react-hooks-guide)
```

**行動促進型:**
```markdown
[useStateの使い方を学ぶ](./usestate-guide)
```

**疑問文型:**
```markdown
[React Hooksとは何か？](./what-is-react-hooks)
```

## リンク配置戦略

### 導入部分（高優先度）

```markdown
# React Hooks完全ガイド

React Hooksは、React 16.8で導入された新機能です。
本記事は[React基礎](./react-basics)を理解している方向けの内容です。
まずReactの基本を学びたい方は、先に基礎編をご覧ください。
```

### 本文中（中優先度）

```markdown
## useStateの使い方

useStateは状態管理の基本です。
より複雑な状態管理が必要な場合は、
[useReducerの使い方](./usereducer-guide)も検討しましょう。
```

### まとめ・結論（高優先度）

```markdown
## まとめ

React Hooksの基本を理解できたら、次は以下の記事がおすすめです:

- [カスタムフックの作り方](./custom-hooks) - ロジックの再利用
- [React パフォーマンス最適化](./react-performance) - 高速化手法
```

## トピッククラスター戦略

### ピラーコンテンツとクラスター記事

```
[ピラーページ]
React 完全ガイド
    ↓ リンク
[クラスター記事群]
├─ React Hooks
├─ React Router
├─ State Management
└─ Performance Optimization
    ↑ 全てピラーページにリンクバック
```

**実装例:**
```markdown
# React 完全ガイド（ピラーページ）

## 目次
1. [React Hooksの使い方](./react-hooks)
2. [React Routerの設定](./react-router)
3. [状態管理の選択](./state-management)
4. [パフォーマンス最適化](./performance)

---

# React Hooksの使い方（クラスター記事）

本記事は[React完全ガイド](./react-complete-guide)の一部です。

[← React完全ガイドに戻る](./react-complete-guide)
```

## 内部リンクの数と配分

### 推奨リンク数

```
記事の長さ別推奨リンク数:

短い記事（1000文字未満）: 3-5個
中程度（1000-3000文字）: 5-8個
長い記事（3000文字以上）: 8-12個
```

### リンク配分の例

```markdown
記事全体（3000文字の場合）:

導入部分: 1-2個（基礎知識へのリンク）
本文: 4-6個（関連トピックへのリンク）
まとめ: 2-3個（次のステップへのリンク）
関連記事セクション: 3-5個
```

## リンク切れの防止

### 定期チェック

```bash
# リンク切れチェックツール
npm install -g broken-link-checker

# サイト全体をチェック
blc https://example.com -ro
```

### リダイレクトの設定

```
記事URL変更時は301リダイレクト:

旧URL: /blog/old-react-guide
新URL: /blog/react-hooks-guide
→ 301リダイレクト設定
```

## nofollow の使い分け

### nofollowを付けるべきリンク

```html
<!-- 外部リンク（信頼性不明） -->
<a href="https://external-site.com" rel="nofollow noopener noreferrer">
  外部サイト
</a>

<!-- ユーザー生成コンテンツ内のリンク -->
<!-- コメント欄のリンク等 -->
```

### nofollowを付けないリンク

```html
<!-- 内部リンク（自サイト内） -->
<a href="/blog/related-article">関連記事</a>

<!-- 信頼できる外部リンク（公式ドキュメント等） -->
<a href="https://react.dev" rel="noopener noreferrer">
  React公式ドキュメント
</a>
```

## 内部リンクレポート

### Google Search Console で確認

```
1. Search Console にログイン
2. 「リンク」セクションを開く
3. 「内部リンク」を確認
4. リンクが少ないページを特定
5. 適切なページから内部リンクを追加
```

### 最もリンクされているページ

```
上位ページ:
1. トップページ (500リンク)
2. React完全ガイド (120リンク)
3. TypeScript入門 (80リンク)

→ これらのページから他記事へリンクを増やす
```

## チェックリスト

### 記事公開時
- [ ] 関連記事へ3-5個のリンク
- [ ] アンカーテキストが説明的
- [ ] ピラーページへのリンクバック
- [ ] 目次（内部アンカーリンク）

### 定期メンテナンス
- [ ] リンク切れチェック（月1回）
- [ ] 新記事へのリンク追加
- [ ] 古い記事の内部リンク見直し
- [ ] Search Console で内部リンク確認

### 品質チェック
- [ ] 自然な文脈に配置
- [ ] リンクテキストが重複していない
- [ ] ユーザーにとって有益
- [ ] クリックしやすい配置
