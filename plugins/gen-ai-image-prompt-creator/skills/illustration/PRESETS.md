# プリセット集

よく使用するプロンプト設定のプリセット。素早く高品質なプロンプトを生成できます。

---

## プリセット1: レトロなオブジェクト

80-90年代のノスタルジックな雰囲気を持つレトロオブジェクトをローファイアニメスタイルで描画。

### 適用対象
- レトロガジェット（カメラ、ウォークマン、ゲーム機）
- ヴィンテージ日用品（電話、時計、ラジオ）
- 懐かしい文房具や小物

### 設定

```yaml
色彩:
  ベース: サンセットオレンジ (#FF6B35) - 30%
  アクセント: ティール (#008B8B) - 30%
  サブ: ダスティピンク (#D4A5A5) - 20%
  ハイライト: クリームイエロー (#FFFACD) - 20%

スタイル: ローファイアニメ、柔らかい線、グレイン質感
光源: ゴールデンアワー、左斜め45度、温かみ(3500K)
視点: 3/4ビュー、クローズアップ〜ミディアム
雰囲気: ノスタルジック、静かな郷愁
```

### ポジティブプロンプト
```
[オブジェクト名], vintage aesthetic with well-used texture,
three-quarter view from slightly elevated angle,
warm golden hour light from 45-degree angle,
retro 80s palette: sunset orange (#FF6B35), teal (#008B8B),
lo-fi anime style, soft linework, subtle grain texture,
nostalgic and peaceful mood,
high quality professional illustration
```

### ネガティブプロンプト
```
hyper-realistic, 3D CGI, modern sleek design,
overly saturated, harsh lighting, cluttered background
```

### 推奨パラメータ
- **Midjourney**: --ar 4:3 --v 6 --stylize 500
- **Stable Diffusion**: Steps 35-45, CFG 7-9

---

## プリセット2: ゆるふわインコ

手描き風の温かみのあるタッチで描く、ふわふわに膨らんだインコの癒し系イラスト。

### 適用対象
- コザクラインコ（ピーチフェイス）
- セキセイインコ、オカメインコなどの小鳥
- ハムスター、ウサギなどの小動物

### 設定

```yaml
色彩:
  ベース: ピーチピンク (#FFE5D9) - 30%
  サブ1: 淡いイエロー (#FFF9C4) - 25%
  サブ2: ミントグリーン (#C8E6C9) - 25%
  アクセント: ライトコーラル (#FFB3BA) - 20%

スタイル: 手描き風、水彩テクスチャ、ゆるキャラ
光源: 柔らかい自然光、均一、影は最小限
視点: 正面または斜め前、クローズアップ
雰囲気: 癒し系、ほのぼの、温かい
```

### ポジティブプロンプト
```
[鳥の種類] fluffed up into round fluffy ball,
gentle expression, relaxed cozy pose,
soft pastel colors (peachy pink #FFE5D9, light yellow #FFF9C4),
hand-drawn style, soft brush strokes, watercolor texture,
kawaii yurufuwa aesthetic,
soft diffused lighting, minimal shadows,
simple white background, centered composition,
healing heartwarming atmosphere
```

### ネガティブプロンプト
```
realistic photography, 3D render, hyper-detailed,
harsh lines, bold saturated colors, dark tones,
complex background, dramatic lighting, aggressive pose
```

### 推奨パラメータ
- **Midjourney**: --ar 1:1 --v 6 --stylize 400
- **DALL-E 3**: Style: Illustration
- **Stable Diffusion**: Steps 25-35, CFG 7-10

---

## プリセットの使い方

1. 「レトロなオブジェクトのプリセットで○○のプロンプトを作って」
2. 設定がベースとして適用される
3. オブジェクト固有の詳細を追加してプロンプト生成

---

## 今後追加予定

- ミニマリスト商品写真
- ファンタジーイラスト
- アーバンストリート（サイバーパンク）
- ナチュラル&オーガニック
- ポップアートスタイル
- 水彩画風
