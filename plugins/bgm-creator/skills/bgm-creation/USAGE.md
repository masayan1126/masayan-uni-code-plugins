# BGM Creation & YouTube Upload - 使い方ガイド

## 完全なワークフロー

### ステップ1: プロンプト生成

```bash
# ジャンル一覧を確認
python3 scripts/generate_prompt.py --list

# 鋼田テフロン風のプロンプトを生成
python3 scripts/generate_prompt.py --genre kouda_teflon_style
```

### ステップ2: Sunoで音楽生成

1. https://suno.ai/ にアクセス
2. 「Create」→「Custom Mode」を選択
3. 「Style of Music」欄に生成されたプロンプトを貼り付け
4. 「Create」をクリックして音楽を生成
5. 生成された音楽をダウンロード

### ステップ3: 動画作成

1. ダウンロードした音楽を使用して動画を編集
2. 完成した動画を配置
3. サムネイル画像を配置（動画と同じ名前）

### ステップ4: メタデータ生成

```bash
python3 scripts/generate_metadata.py --video your_video.mp4 --genre kouda_teflon_style
```

### ステップ5: YouTubeアップロード

```bash
python3 scripts/upload_youtube.py --video your_video.mp4
```

---

## コマンドオプション

### generate_prompt.py

```bash
--genre, -g        # ジャンルキー（必須）
--list, -l         # ジャンル一覧表示
--output, -o       # 出力ディレクトリ
--no-variation     # バリエーションなしで生成
--custom, -c       # カスタム要素追加
```

### generate_metadata.py

```bash
--video, -v        # 動画ファイルパス
--genre, -g        # ジャンル明示（自動検出を上書き）
--title-suffix, -t # タイトルサフィックス
--privacy, -p      # 公開設定（public/unlisted/private）
--output, -o       # 出力JSONファイル
```

### upload_youtube.py

```bash
--video, -v        # 動画ファイルパス（必須）
--metadata, -m     # メタデータJSONファイル
--thumbnail, -th   # サムネイル画像ファイル
--credentials, -c  # OAuth認証情報
--token, -t        # トークンファイル
```

---

## 対応ジャンル

| ジャンルキー | 名前 | BPM | キー |
|------------|------|-----|------|
| kouda_teflon_style | 鋼田テフロン風 | 85-95 | C minor |
| lofi_synth | Lo-Fi Synth | 70-80 | A minor |
| chillout | Chillout | 60-75 | G major |
| synthwave | Synthwave | 110-125 | D minor |
| vaporwave | Vaporwave | 60-70 | E major |
| cyberpunk_rnb | Cyberpunk R&B | 80-95 | F# minor |
| electro_pop | Electro Pop | 120-130 | C major |
| hood_rap | Hood Rap | 85-95 | G minor |
| gangster_trap | Gangster Trap | 130-150 | B minor |
| spoken_rap | Spoken Rap | 80-95 | A minor |
| lofi_chillout | Lo-Fi Chillout | 70-85 | - |

---

## セキュリティ注意事項

- `credentials.json` と `token.json` は機密情報です
- **絶対にGitリポジトリにコミットしないでください**
