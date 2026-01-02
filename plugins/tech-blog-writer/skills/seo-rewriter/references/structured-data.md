# 構造化データ（JSON-LD）ガイド

検索エンジンに記事内容を正確に伝えるための構造化データ実装ガイドです。

## 構造化データとは

JSON-LD形式でページ内容を記述し、検索エンジンに情報を伝える仕組みです。

**メリット:**
- リッチリザルト（Rich Results）での表示
- 検索エンジンの理解度向上
- CTR（クリック率）の向上
- 音声検索での表示率向上

## テックブログで使うスキーマ

### 1. TechArticle（技術記事）

最も基本的な技術記事用スキーマ:

```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "React Hooks完全ガイド｜useState/useEffectの使い方と実践例7選",
  "description": "React Hooksの基礎から実践まで徹底解説。useState、useEffect、カスタムフックの使い方を実例7つで学べます。",
  "image": "https://example.com/images/react-hooks-guide.png",
  "author": {
    "@type": "Person",
    "name": "山田太郎",
    "url": "https://example.com/author/yamada",
    "jobTitle": "シニアフロントエンドエンジニア",
    "alumniOf": "東京大学",
    "sameAs": [
      "https://twitter.com/yamada",
      "https://github.com/yamada"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "name": "Tech Blog",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "datePublished": "2024-01-15T09:00:00+09:00",
  "dateModified": "2024-10-20T14:30:00+09:00",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/blog/react-hooks-guide"
  },
  "keywords": ["React", "Hooks", "useState", "useEffect", "JavaScript"],
  "articleSection": "Web Development",
  "wordCount": 3500,
  "inLanguage": "ja-JP",
  "proficiencyLevel": "Beginner"
}
```

### 2. HowTo（チュートリアル記事）

手順を説明する記事向け:

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "React HooksでTodoアプリを作る方法",
  "description": "React Hooksを使ってTodoアプリを作成する5ステップのチュートリアル",
  "image": "https://example.com/images/todo-app-tutorial.png",
  "totalTime": "PT30M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "JPY",
    "value": "0"
  },
  "tool": [
    {
      "@type": "HowToTool",
      "name": "Node.js 18+"
    },
    {
      "@type": "HowToTool",
      "name": "React 18"
    }
  ],
  "supply": [
    {
      "@type": "HowToSupply",
      "name": "テキストエディタ（VS Code推奨）"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "プロジェクトのセットアップ",
      "text": "Viteを使ってReactプロジェクトを作成します",
      "url": "https://example.com/blog/todo-app-tutorial#step1",
      "image": "https://example.com/images/step1.png"
    },
    {
      "@type": "HowToStep",
      "name": "Todoコンポーネントの作成",
      "text": "useStateを使ってTodoの状態管理を実装します",
      "url": "https://example.com/blog/todo-app-tutorial#step2",
      "image": "https://example.com/images/step2.png"
    },
    {
      "@type": "HowToStep",
      "name": "追加機能の実装",
      "text": "Todo追加フォームを作成します",
      "url": "https://example.com/blog/todo-app-tutorial#step3"
    },
    {
      "@type": "HowToStep",
      "name": "削除機能の実装",
      "text": "Todoを削除する機能を追加します",
      "url": "https://example.com/blog/todo-app-tutorial#step4"
    },
    {
      "@type": "HowToStep",
      "name": "完了/未完了の切り替え",
      "text": "Todoの状態を切り替える機能を実装します",
      "url": "https://example.com/blog/todo-app-tutorial#step5"
    }
  ]
}
```

### 3. FAQPage（FAQ記事）

よくある質問を含む記事向け:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "React Hooksとは何ですか?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "React Hooksは、React 16.8で導入された機能で、関数コンポーネントで状態管理や副作用を扱えるようにするものです。useStateやuseEffectなどのフック関数を使うことで、クラスコンポーネントを書かずに、よりシンプルなコードで複雑な機能を実装できます。"
      }
    },
    {
      "@type": "Question",
      "name": "useStateとuseReducerの違いは何ですか?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "useStateは単純な状態管理に適しており、useReducerは複雑な状態ロジックやアクション履歴の管理に適しています。useStateは直接値を更新しますが、useReducerはアクションを通じて状態を更新するため、複雑な状態遷移をテストしやすくなります。"
      }
    },
    {
      "@type": "Question",
      "name": "useEffectはいつ使うべきですか?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "useEffectは副作用（side effects）を扱う際に使用します。具体的には、データのフェッチ、DOM操作、イベントリスナーの登録/解除、タイマーの設定などです。コンポーネントのレンダリング後に実行したい処理がある場合に使用します。"
      }
    }
  ]
}
```

### 4. BreadcrumbList（パンくずリスト）

サイト構造を示すパンくず:

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "ホーム",
      "item": "https://example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "ブログ",
      "item": "https://example.com/blog"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "React",
      "item": "https://example.com/blog/category/react"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "React Hooks完全ガイド",
      "item": "https://example.com/blog/react-hooks-guide"
    }
  ]
}
```

### 5. Person / Organization（著者・組織情報）

著者や組織の情報:

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "山田太郎",
  "url": "https://example.com/author/yamada",
  "image": "https://example.com/images/yamada.jpg",
  "jobTitle": "シニアフロントエンドエンジニア",
  "worksFor": {
    "@type": "Organization",
    "name": "Tech Company Inc."
  },
  "alumniOf": {
    "@type": "EducationalOrganization",
    "name": "東京大学"
  },
  "knowsAbout": ["React", "TypeScript", "Web Development", "JavaScript"],
  "sameAs": [
    "https://twitter.com/yamada",
    "https://github.com/yamada",
    "https://linkedin.com/in/yamada"
  ]
}
```

## 実装方法

### HTMLへの埋め込み

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>React Hooks完全ガイド</title>

  <!-- TechArticle -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "React Hooks完全ガイド",
    ...
  }
  </script>

  <!-- BreadcrumbList -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    ...
  }
  </script>

  <!-- FAQPage -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    ...
  }
  </script>
</head>
<body>
  <!-- 記事内容 -->
</body>
</html>
```

### Reactでの実装

```jsx
import { Helmet } from 'react-helmet-async';

function BlogPost({ article }) {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": article.title,
    "description": article.description,
    "author": {
      "@type": "Person",
      "name": article.author.name
    },
    "datePublished": article.publishedAt,
    "dateModified": article.updatedAt
  };

  return (
    <>
      <Helmet>
        <script type="application/ld+json">
          {JSON.stringify(structuredData)}
        </script>
      </Helmet>

      <article>
        {/* 記事内容 */}
      </article>
    </>
  );
}
```

## テストと検証

### Google Rich Results Test

```
https://search.google.com/test/rich-results
```

1. URLを入力またはコードを貼り付け
2. 「URLをテスト」をクリック
3. エラーや警告をチェック
4. 修正して再テスト

### Schema.org Validator

```
https://validator.schema.org/
```

1. JSON-LDコードを貼り付け
2. バリデーション実行
3. エラーを確認・修正

## よくあるエラーと対処法

### エラー1: 必須プロパティが不足

```json
❌ エラー
{
  "@type": "TechArticle",
  "headline": "記事タイトル"
  // author, datePublished が不足
}

✅ 修正後
{
  "@type": "TechArticle",
  "headline": "記事タイトル",
  "author": {
    "@type": "Person",
    "name": "山田太郎"
  },
  "datePublished": "2024-01-15"
}
```

### エラー2: 日付フォーマットが不正

```json
❌ エラー
"datePublished": "2024/01/15"

✅ 修正後
"datePublished": "2024-01-15T09:00:00+09:00"
```

### エラー3: URLが不正

```json
❌ エラー
"image": "/images/article.png" // 相対パス

✅ 修正後
"image": "https://example.com/images/article.png" // 絶対パス
```

## チェックリスト

### 必須実装
- [ ] TechArticle または Article スキーマ
- [ ] author 情報
- [ ] datePublished / dateModified
- [ ] headline / description
- [ ] image（絶対URL）

### 推奨実装
- [ ] BreadcrumbList
- [ ] FAQPage（FAQがある場合）
- [ ] HowTo（チュートリアル記事の場合）
- [ ] Organization / Person 詳細情報

### 検証
- [ ] Rich Results Test合格
- [ ] Schema.org Validator合格
- [ ] すべてのURLが絶対パス
- [ ] 日付がISO 8601形式
