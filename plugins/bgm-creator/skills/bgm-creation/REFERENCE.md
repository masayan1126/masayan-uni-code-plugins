# Technical Reference

BGM Creation & YouTube Upload Agentの技術的な参考情報です。

## 作業フェーズ詳細

### フェーズ1: Sunoプロンプト生成

**対話の流れ**:

1. **ジャンル選択**
   - FORMS.mdの11種類のジャンルをAskUserQuestionで提示
   - ユーザーの選択を受け取る

2. **プロンプト生成実行**
   ```bash
   python3 scripts/generate_prompt.py --genre <選択されたジャンル>
   ```

3. **結果提示**
   - 生成されたプロンプトをユーザーに提示
   - 次のステップを案内:
     - 「このプロンプトをコピーしてSuno（https://suno.ai/）で使用してください」
     - 「音楽生成後、動画を作成して配置してください」

---

### フェーズ2-A: YouTubeメタデータ生成

1. **動画ファイル確認**
2. **ジャンル確認**（ファイル名から自動検出またはユーザーに質問）
3. **メタデータ生成実行**
   ```bash
   python3 scripts/generate_metadata.py --video "<ファイル名>" --genre <ジャンル>
   ```
4. **生成結果確認**

---

### フェーズ2-B: YouTubeアップロード

1. **前提条件チェック**（動画ファイル、メタデータファイル、認証情報）
2. **アップロード確認**
3. **アップロード実行**
   ```bash
   python3 scripts/upload_youtube.py --video "<ファイル名>"
   ```
4. **結果報告**（YouTube URL、Video ID）

---

## YouTube Data API v3

### 必要な権限スコープ

```python
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
```

### 認証設定手順

1. Google Cloud Consoleでプロジェクト作成
2. YouTube Data API v3を有効化
3. OAuth 2.0認証情報を作成（デスクトップアプリ）
4. `credentials.json`をダウンロードして配置

### API制限

- 1日あたりのクォータ: 10,000ユニット
- 動画アップロード: 1回あたり約1,600ユニット消費
- 最大ファイルサイズ: 128GB

---

## Suno プロンプト作成ガイドライン

### 効果的なプロンプトの5つの原則

1. **ジャンル・テーマ・テンポ・キーを具体的に伝える**
2. **複数の要素を組み合わせて独創性を出す**
3. **具体的な楽器名を使う**
4. **雰囲気・ムードを具体的に表現**
5. **200文字以内に収める**

### プロンプト構造テンプレート

```
[ジャンル1] + [ジャンル2], [BPM] BPM, [キー], [具体的楽器1], [具体的楽器2], [プロダクション特性], [ムード/雰囲気]
```

---

## YouTubeメタデータ生成ガイドライン

### タイトル形式

**必須形式**: `English Title | カタカナ日本語 - Suffix`

**例**:
- `Soulful Japanese Hip-Hop R&B Mix | ソウルフル ジャパニーズ ヒップホップ R&B ミックス - Smooth Urban Beats`

### 説明欄の構造

**英語セクション** → **日本語セクション** → **ハッシュタグ**

### ハッシュタグ戦略

- 15-20個（英語 + 日本語）
- SEOを意識したタグ選定

### サムネイル

- 推奨サイズ: 1280x720px (16:9)
- フォーマット: JPG/PNG
- 動画ファイルと同じ名前で自動検出

---

## トラブルシューティング

### YouTube API認証エラー

1. `credentials.json`が正しく配置されているか確認
2. Google Cloud Consoleでアプリが有効か確認
3. `token.json`を削除して再認証

### クォータ超過

- 翌日まで待つ（クォータは日次リセット）
- Google Cloud Consoleでクォータ増加リクエスト
