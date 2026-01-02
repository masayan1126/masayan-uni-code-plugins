# コンテンツ更新ガイド

技術記事の鮮度を保ち、最新情報に更新するためのガイドです。

## なぜ更新が重要か

- Googleは鮮度を評価要因に含む
- 古い情報は読者の信頼を損なう
- 非推奨APIの使用は実害がある
- 定期更新でクロール頻度が上がる

## 更新すべき情報の種類

### 1. バージョン情報

**更新対象:**
- ライブラリ・フレームワークのバージョン
- 言語のバージョン
- ツールのバージョン

**例:**
```markdown
❌ 古い表現
React 16でHooksが導入されました。

✅ 更新後
React 16.8でHooksが導入され、現在はReact 18が最新版です（2024年10月時点）。
React 18では、Concurrent Renderingなどの新機能が追加されています。
```

### 2. 非推奨API・メソッド

**更新対象:**
- 非推奨になったAPI
- 推奨されなくなった書き方
- セキュリティ上問題のある手法

**例:**
```markdown
❌ 古い表現（React 16以前）
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  componentDidMount() {
    console.log('マウントされました');
  }

  render() {
    return <div>{this.state.count}</div>;
  }
}

✅ 更新後（React Hooks使用）
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log('マウントされました');
  }, []);

  return <div>{count}</div>;
}

**注記:**
クラスコンポーネントも引き続き使用可能ですが、
新規開発ではHooksを使った関数コンポーネントが推奨されています。
```

### 3. ベストプラクティスの変化

**更新対象:**
- 推奨される設計パターン
- コーディング規約の変化
- パフォーマンス最適化手法

**例:**
```markdown
❌ 古い表現
Proptypesを使って型チェックを行います。

\`\`\`javascript
import PropTypes from 'prop-types';

Component.propTypes = {
  name: PropTypes.string.isRequired
};
\`\`\`

✅ 更新後
TypeScriptを使った型安全な開発が主流になっています。

\`\`\`typescript
interface Props {
  name: string;
}

function Component({ name }: Props) {
  return <div>{name}</div>;
}
\`\`\`

**補足:**
PropTypesは現在も使用可能ですが、TypeScriptによる
静的型チェックの方が強力で、開発体験も向上します。
```

### 4. 依存パッケージの変更

**更新対象:**
- インストールコマンド
- パッケージ名の変更
- 新しいパッケージへの移行

**例:**
```markdown
❌ 古い表現
\`\`\`bash
npm install --save react-router
\`\`\`

✅ 更新後
\`\`\`bash
# React Router v6（2024年10月時点の最新版）
npm install react-router-dom@6
\`\`\`

**主な変更点:**
- `Switch` → `Routes` に変更
- `component` prop → `element` prop に変更
- ネストされたルートの記法が簡潔に
```

### 5. ツール・環境の変化

**更新対象:**
- ビルドツール（Webpack → Vite等）
- 開発環境のセットアップ
- デプロイ方法

**例:**
```markdown
❌ 古い表現
Create React Appでプロジェクトを作成します。

\`\`\`bash
npx create-react-app my-app
\`\`\`

✅ 更新後
Viteを使った高速な開発環境構築が推奨されています。

\`\`\`bash
npm create vite@latest my-app -- --template react
\`\`\`

**Viteのメリット:**
- 起動が高速（ESM利用）
- HMRが高速
- ビルドも高速（Rollup使用）
```

### 6. セキュリティ関連

**更新対象:**
- 脆弱性のある書き方
- セキュリティガイドラインの変更
- 認証・認可の最新手法

**例:**
```markdown
❌ 古い表現
\`\`\`javascript
// dangerouslySetInnerHTMLの使用
<div dangerouslySetInnerHTML={{__html: userInput}} />
\`\`\`

✅ 更新後
\`\`\`javascript
// XSS対策: サニタイズライブラリを使用
import DOMPurify from 'dompurify';

const sanitizedHTML = DOMPurify.sanitize(userInput);
<div dangerouslySetInnerHTML={{__html: sanitizedHTML}} />
\`\`\`

**セキュリティ注意:**
ユーザー入力を直接HTMLとして表示するのは危険です。
必ずサニタイズ処理を行ってください。
```

## 更新作業のワークフロー

### ステップ1: 情報の鮮度チェック

```markdown
チェック項目:
□ 公開日・最終更新日を確認
□ 記事内のバージョン番号を確認
□ 使用しているAPIが非推奨になっていないか確認
□ リンク切れがないか確認
□ 競合記事の最新状況を確認
```

### ステップ2: 最新情報の調査

```markdown
情報源:
□ 公式ドキュメントの変更履歴
□ GitHubのCHANGELOG
□ リリースノート
□ 公式ブログ
□ コミュニティの動向（Reddit, X等）
```

### ステップ3: 更新内容の決定

```markdown
優先度:
高: セキュリティ、非推奨API、バージョン情報
中: ベストプラクティス、ツールの変更
低: 細かい表現の改善、リンク追加
```

### ステップ4: 更新の実施

```markdown
更新時のルール:
1. 古い情報を削除せず、「更新後」として併記
2. 変更理由を明記
3. 移行方法を示す
4. 最終更新日を記載
```

### ステップ5: 検証

```markdown
検証項目:
□ コードサンプルが動作するか確認
□ リンクが有効か確認
□ 情報の整合性を確認
□ 最新バージョンとの整合性を確認
```

## 更新履歴の記載方法

### パターン1: 記事冒頭に記載

```markdown
# React Hooks完全ガイド

**最終更新: 2024年10月20日**

**更新履歴:**
- 2024-10-20: React 18の新機能について追記
- 2024-05-15: useTransitionの説明を追加
- 2023-12-01: コード例を最新のベストプラクティスに更新
- 2023-06-15: 初版公開

---

本記事では、React Hooksの基本から...
```

### パターン2: 記事末尾に記載

```markdown
## 更新履歴

| 日付 | 更新内容 |
|------|---------|
| 2024-10-20 | React 18の新機能について追記 |
| 2024-05-15 | useTransitionの説明を追加 |
| 2023-12-01 | コード例を最新のベストプラクティスに更新 |
| 2023-06-15 | 初版公開 |
```

### パターン3: 該当箇所に注記

```markdown
## useStateの使い方

> **更新情報（2024年10月）:**
> React 18では、自動バッチングが標準で有効になりました。
> これにより、複数のsetStateが自動的にバッチ処理されます。

\`\`\`javascript
// React 18では、以下が1回のレンダリングでバッチ処理される
setCount(c => c + 1);
setFlag(f => !f);
\`\`\`
```

## 技術トレンドの追跡

### React エコシステムの例

```markdown
## 最新トレンド（2024年）

### Server Components
React 18で導入されたServer Componentsが主流に。

**メリット:**
- バンドルサイズ削減
- 初期表示の高速化
- SEO改善

### ビルドツールの進化
Vite、Turbopackなど高速ビルドツールが台頭。

### 状態管理の変化
Zustand、Jotaiなど軽量ライブラリが人気。
```

## チェックリスト

### 定期更新（3-6ヶ月ごと）
- [ ] バージョン情報の確認・更新
- [ ] リンク切れのチェック
- [ ] 最新ベストプラクティスの反映
- [ ] 最終更新日の記載

### 緊急更新（必要時）
- [ ] セキュリティ脆弱性の修正
- [ ] 重大なバグ情報の追記
- [ ] 非推奨API使用箇所の修正

### 品質チェック
- [ ] コードが最新バージョンで動作
- [ ] スクリーンショットが最新UI
- [ ] 情報の正確性
- [ ] 読者からのフィードバック反映
