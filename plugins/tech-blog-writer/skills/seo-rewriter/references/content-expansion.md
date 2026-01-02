# コンテンツ拡充ガイド

検索意図を満たし、読者により多くの価値を提供するためのコンテンツ拡充アイデア集です。

## FAQセクションの追加

### FAQ作成のポイント

読者がよく検索する質問に先回りして答えます。

**質問の見つけ方:**
- Google「他の人はこちらも質問」
- ラッコキーワード（サジェストキーワード）
- Yahoo!知恵袋、Stack Overflow
- コメント欄の質問

### テックブログ向けFAQテンプレート

```markdown
## よくある質問（FAQ）

### Q1: React Hooksとクラスコンポーネントはどちらがおすすめですか？

A: 新規プロジェクトではReact Hooksを推奨します。理由は以下の通り:

- コード量が少なく、読みやすい
- ロジックの再利用が容易（カスタムフック）
- React公式が推奨している

ただし、既存のクラスコンポーネントを無理に書き換える必要はありません。

### Q2: useStateとuseReducerの使い分けは？

A: 以下の基準で使い分けます:

**useStateを使う場合:**
- 単純な状態管理（文字列、数値、真偽値）
- 状態の更新ロジックがシンプル

**useReducerを使う場合:**
- 複雑な状態オブジェクト
- 複数の状態が相互に関連
- 状態更新ロジックをテストしたい

### Q3: useEffectはいつ実行されますか？

A: useEffectの実行タイミングは、依存配列によって決まります:

\`\`\`javascript
// パターン1: マウント時のみ
useEffect(() => {
  console.log('マウント時');
}, []);

// パターン2: 特定の値が変わった時
useEffect(() => {
  console.log('countが変わった時');
}, [count]);

// パターン3: 毎回のレンダリング後
useEffect(() => {
  console.log('毎回実行');
});
\`\`\`
```

### FAQ追加の効果

- 検索意図の充足度向上
- 滞在時間の増加
- 構造化データ（FAQPage）の実装が可能
- 音声検索での表示率向上

## 実践例・コード例の追加

### 実例を増やす理由

- 理解度が劇的に向上
- コピペで試せる
- 検索意図（実装方法を知りたい）を満たす
- ページ滞在時間が延びる

### 実例追加のパターン

#### パターン1: 難易度別の実例

```markdown
## useStateの実装例

### 初級: カウンター機能

\`\`\`javascript
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>カウント: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
    </div>
  );
}
\`\`\`

### 中級: フォーム入力管理

\`\`\`javascript
function UserForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <form>
      <input
        name="name"
        value={formData.name}
        onChange={handleChange}
      />
      <input
        name="email"
        value={formData.email}
        onChange={handleChange}
      />
    </form>
  );
}
\`\`\`

### 上級: バリデーション付きフォーム

\`\`\`javascript
function ValidatedForm() {
  const [formData, setFormData] = useState({ email: '' });
  const [errors, setErrors] = useState({});

  const validate = (data) => {
    const newErrors = {};
    if (!data.email.includes('@')) {
      newErrors.email = '有効なメールアドレスを入力してください';
    }
    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = validate(formData);
    if (Object.keys(validationErrors).length === 0) {
      console.log('送信成功');
    } else {
      setErrors(validationErrors);
    }
  };

  // ... 省略
}
\`\`\`
```

#### パターン2: ユースケース別の実例

```markdown
## useEffectの実践例

### ユースケース1: データフェッチ

\`\`\`javascript
function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('https://api.example.com/users')
      .then(res => res.json())
      .then(data => {
        setUsers(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>読み込み中...</p>;
  return <ul>{users.map(user => <li>{user.name}</li>)}</ul>;
}
\`\`\`

### ユースケース2: イベントリスナー登録

\`\`\`javascript
function WindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });

  useEffect(() => {
    const handleResize = () => {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    };

    window.addEventListener('resize', handleResize);

    // クリーンアップ
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return <p>Width: {size.width}px</p>;
}
\`\`\`
```

## 比較表の追加

### 比較表が効果的な場面

- 複数の選択肢を比較したい
- 特徴・違いを整理したい
- 意思決定をサポートしたい

### 比較表のテンプレート

```markdown
## React Hooksの比較

| Hook | 用途 | 複雑度 | 使用頻度 | ユースケース |
|------|------|--------|----------|--------------|
| useState | 状態管理 | ★☆☆ | 非常に高い | フォーム、トグル、カウンター |
| useEffect | 副作用処理 | ★★☆ | 非常に高い | データフェッチ、イベント登録 |
| useContext | コンテキスト | ★★☆ | 中 | テーマ、認証状態の共有 |
| useReducer | 複雑な状態 | ★★★ | 中 | 複数状態の管理 |
| useMemo | メモ化 | ★★☆ | 低 | 重い計算の最適化 |
| useCallback | コールバック | ★★☆ | 低 | 関数の再生成防止 |

## useState vs useReducer 詳細比較

| 比較項目 | useState | useReducer |
|---------|----------|-----------|
| 学習コスト | 低い | やや高い |
| コード量 | 少ない | やや多い |
| テストのしやすさ | 普通 | 高い（reducerを単独テスト可） |
| 適している場面 | シンプルな状態 | 複雑な状態ロジック |
| デバッグのしやすさ | 普通 | 高い（アクション履歴追跡可） |
```

## トラブルシューティングセクション

### よくあるエラーと解決法

```markdown
## トラブルシューティング

### エラー1: "Rendered more hooks than during the previous render"

**原因:**
条件分岐の中でHooksを呼び出している

\`\`\`javascript
// ❌ 間違った使い方
function Component() {
  if (condition) {
    const [state, setState] = useState(0); // 条件内でHooks
  }
}
\`\`\`

**解決法:**
Hooksはコンポーネントのトップレベルで呼び出す

\`\`\`javascript
// ✅ 正しい使い方
function Component() {
  const [state, setState] = useState(0); // トップレベル

  if (condition) {
    // ここで state を使用
  }
}
\`\`\`

### エラー2: "Can't perform a React state update on an unmounted component"

**原因:**
コンポーネントがアンマウントされた後に状態更新を試みている

**解決法:**
クリーンアップ関数で非同期処理をキャンセル

\`\`\`javascript
useEffect(() => {
  let isMounted = true;

  fetch('/api/data')
    .then(res => res.json())
    .then(data => {
      if (isMounted) { // マウント状態をチェック
        setData(data);
      }
    });

  return () => {
    isMounted = false; // アンマウント時にフラグを変更
  };
}, []);
\`\`\`
```

## チートシート・早見表

```markdown
## React Hooks チートシート

### useState

\`\`\`javascript
const [state, setState] = useState(initialValue);
setState(newValue);
setState(prev => prev + 1); // 前の値を元に更新
\`\`\`

### useEffect

\`\`\`javascript
// パターン1: マウント時のみ
useEffect(() => { /* 処理 */ }, []);

// パターン2: 依存値変更時
useEffect(() => { /* 処理 */ }, [dependency]);

// パターン3: クリーンアップ付き
useEffect(() => {
  /* セットアップ */
  return () => { /* クリーンアップ */ };
}, []);
\`\`\`

### useContext

\`\`\`javascript
const value = useContext(MyContext);
\`\`\`

### useReducer

\`\`\`javascript
const [state, dispatch] = useReducer(reducer, initialState);
dispatch({ type: 'ACTION_TYPE', payload: data });
\`\`\`
```

## 図解・フロー図の追加

```markdown
## useEffectの実行フロー

\`\`\`
[コンポーネントレンダリング]
         ↓
[useEffect実行（副作用）]
         ↓
[依存配列の値を記憶]
         ↓
[再レンダリング発生]
         ↓
[依存配列の値を比較] → 変化なし → [useEffectスキップ]
         ↓
      変化あり
         ↓
[前回のクリーンアップ実行]
         ↓
[useEffect再実行]
\`\`\`
```

## 関連リソース・参考資料

```markdown
## さらに学ぶためのリソース

### 公式ドキュメント
- [React 公式 - Hooks API Reference](https://react.dev/reference/react)
- [React 公式 - Hooks FAQ](https://react.dev/learn#using-hooks)

### おすすめ記事
- カスタムフックの作り方（本サイト内部リンク）
- React パフォーマンス最適化（本サイト内部リンク）

### 動画チュートリアル
- React Hooksの基本（YouTube）
- 実践的なカスタムフック作成（Udemy）

### コミュニティ
- React 日本ユーザーグループ
- Stack Overflow - React タグ
```

## コンテンツ拡充チェックリスト

### 必須追加項目
- [ ] FAQセクション（最低3-5個）
- [ ] 実践例（最低3個、難易度別）
- [ ] トラブルシューティング

### 推奨追加項目
- [ ] 比較表
- [ ] チートシート・早見表
- [ ] 図解・フロー図
- [ ] 関連リソース

### オプション項目
- [ ] 動画埋め込み
- [ ] インタラクティブデモ
- [ ] ダウンロード可能な資料
- [ ] コメント欄
