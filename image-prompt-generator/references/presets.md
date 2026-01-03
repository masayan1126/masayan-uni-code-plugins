# 画像生成プロンプト プリセット集

このファイルには、よく使用するプロンプト設定をプリセットとして保存しています。新しいプロンプトを作成する際、これらのプリセットをベースにオブジェクトや詳細を変更するだけで、素早く高品質なプロンプトが生成できます。

---

## プリセット1: レトロなオブジェクト

### 概要
80-90年代のノスタルジックな雰囲気を持つレトロオブジェクトを、ローファイアニメスタイルで描画するプリセット。温かみのあるゴールデンアワーの光と、レトロ80sカラーパレットが特徴。

### 適用対象
- レトロなガジェット（カメラ、ウォークマン、ゲーム機など）
- ヴィンテージな日用品（電話、時計、ラジオなど）
- 懐かしい文房具や小物

### 設定詳細

#### 色彩・カラーパレット
```yaml
ベースカラー: サンセットオレンジ (#FF6B35) - 30%
アクセントカラー: ティール (#008B8B) - 30%
サブカラー: ダスティピンク (#D4A5A5) - 20%
ハイライト: クリームイエロー (#FFFACD) - 20%
全体のトーン: やや彩度を落としたヴィンテージ感、温かみのある色温度
```

#### スタイル・画風
```yaml
芸術様式: ローファイアニメスタイル
特徴: 柔らかい線、落ち着いた色彩、シンプルな描写
質感: 若干のグレイン（粒子感）、アナログな質感
時代感: 80-90年代のアニメ美学を現代的に解釈
```

#### 光源・照明
```yaml
光の種類: ゴールデンアワーの自然光
光の方向: 左斜め45度から
光の質: 柔らかく拡散した温かい光
色温度: 温かみのある3500K前後
効果: オブジェクト本体に温かいハイライト、柔らかい影
```

#### 視点・構図
```yaml
カメラアングル: やや斜め上から（3/4ビュー）
距離: クローズアップ～ミディアムショット
構図: オブジェクトを画面中央やや右に配置、三分割法を意識
被写界深度: やや浅め、背景はソフトにぼかす
```

#### 雰囲気・効果
```yaml
ムード: ノスタルジック、懐かしさ、静かな郷愁
テーマ: レトロテクノロジー・オブジェクトへの愛着
感情: 穏やかで温かい、タイムレスな魅力
```

### プロンプトテンプレート

#### ポジティブプロンプト
```
[オブジェクト名とその詳細な特徴],
vintage aesthetic with well-used texture,
[オブジェクト固有のディテール],

three-quarter view from slightly elevated angle,
close-up to medium shot composition,
object positioned center-right following rule of thirds,
shallow depth of field with softly blurred background,

warm golden hour natural light from 45-degree angle left,
soft diffused sunlight creating warm highlights,
gentle shadows, warm color temperature (3500K),
cozy and nostalgic atmosphere,

retro 80s color palette:
sunset orange (#FF6B35) and teal (#008B8B) as main colors,
dusty pink (#D4A5A5) and cream yellow (#FFFACD) accents,
slightly desaturated for vintage feel,

lo-fi anime style,
soft linework with gentle gradients,
calm and subdued color rendering,
simple clean illustration,
subtle grain texture for analog quality,
80s-90s anime aesthetic with modern interpretation,

nostalgic and peaceful mood,
quiet sentimentality toward retro object,
timeless charm with warm emotional tone,

high quality professional digital illustration,
detailed rendering with soft brush strokes
```

#### ネガティブプロンプト
```
hyper-realistic photography, 3D CGI rendering,
modern sleek design, minimalist contemporary style,
overly saturated vivid colors, harsh fluorescent lighting,
cluttered busy background, too many objects,
sharp dramatic shadows, high contrast,
photorealistic texture, ultra-modern appearance,
cold color temperature, sterile atmosphere,
pixelated low quality, messy composition,
anime characters or faces, overly complex details
```

### 使用例

#### 例1: レトロデジタルカメラ
```
retro compact digital camera from early 2000s,
rounded body design with small LCD screen,
vintage aesthetic with well-used texture,
buttons and dials with reflective lens,

[共通テンプレートを適用]
```

#### 例2: ヴィンテージウォークマン
```
vintage Sony Walkman-style portable cassette player,
classic rectangular design with foam headphones,
vintage aesthetic with slightly worn metallic finish,
play/stop buttons and cassette window visible,

[共通テンプレートを適用]
```

#### 例3: レトロゲーム機コントローラー
```
retro game console controller from 90s era,
chunky design with colorful buttons,
vintage aesthetic with smooth plastic texture,
D-pad and action buttons clearly visible,

[共通テンプレートを適用]
```

### Midjourney推奨パラメータ
```
--ar 4:3
--v 6
--stylize 500
--quality 2
```

### Stable Diffusion推奨設定
```
Steps: 35-45
CFG Scale: 7-9
Sampler: DPM++ 2M Karras or Euler a
```

---

## プリセットの追加方法

新しいプリセットを追加する場合は、以下の構造に従ってください:

```markdown
## プリセット名: [名前]

### 概要
[プリセットの説明]

### 適用対象
- [使用できる被写体やシーン]

### 設定詳細
[色彩、スタイル、光源、視点、雰囲気の詳細]

### プロンプトテンプレート
[ポジティブプロンプトとネガティブプロンプトのテンプレート]

### 使用例
[具体的な使用例]

### 推奨パラメータ
[AI別の推奨設定]
```

---

## プリセット2: ゆるふわコザクラインコ

### 概要
手描き風の温かみのあるタッチで描く、ふわふわに膨らんだコザクラインコのイラストプリセット。パステルカラーと柔らかいブラシストロークが特徴で、癒し系のゆるキャラ風デザイン。

### 適用対象
- コザクラインコ（ピーチフェイスドラブバード）
- セキセイインコ、オカメインコなどの小鳥
- ハムスター、ウサギなどの小動物（ゆるふわスタイル）
- ペット動物の癒し系イラスト

### 設定詳細

#### 色彩・カラーパレット
```yaml
ベースカラー: ピーチピンク (#FFE5D9) - 30%
サブカラー1: 淡いイエロー (#FFF9C4) - 25%
サブカラー2: ミントグリーン (#C8E6C9) - 25%
アクセントカラー: ライトコーラル (#FFB3BA) - 20%
全体のトーン: パステル調、低彩度の優しい色使い、明るく柔らかい
```

#### スタイル・画風
```yaml
芸術様式: 手描き風デジタルイラスト、ゆるキャラ風
特徴: 柔らかいブラシストローク、水彩画のような淡い色の重なり
質感: 温かみのある手描き感、線の太さに変化
時代感: 現代的な癒し系イラスト、ゆるふわ（yurufuwa）美学
```

#### 光源・照明
```yaml
光の種類: 柔らかい自然光
光の方向: 全体的に均一、上からの優しい光
光の質: 拡散した柔らかい光、影は薄く柔らかい
色温度: ナチュラルで明るい
効果: 全体的に明るく、影は最小限で優しい
```

#### 視点・構図
```yaml
カメラアングル: 正面または斜め前から
距離: クローズアップ～ミディアムショット
構図: 中央配置、被写体全体がフレームに収まる
被写界深度: シンプル、背景はクリーンな白
```

#### 雰囲気・効果
```yaml
ムード: 癒し系、ほのぼの、温かい
テーマ: 日常の可愛らしさ、リラックス、ほっこり
感情: 優しく穏やか、見ているだけで癒される
```

### プロンプトテンプレート

#### ポジティブプロンプト
```
[鳥の種類] fluffed up into round fluffy ball,
[鳥の特徴的な色や模様],
gentle expression with calm eyes, relaxed and cozy pose,

soft pastel colors (peachy pink #FFE5D9, light yellow #FFF9C4, mint green #C8E6C9),
light coral (#FFB3BA) accents,
pastel tone palette, low saturation gentle colors,

hand-drawn illustration style, soft brush strokes, watercolor-like texture,
warm and gentle line art with varying thickness,
kawaii cute character design, yurufuwa (soft and fluffy) aesthetic,

healing and heartwarming atmosphere, cozy and peaceful mood,

soft diffused natural lighting, minimal soft shadows,
overall bright and even illumination,

simple clean white background, centered composition,
full body or close-up view from front or slight angle,

high quality digital illustration, warm and inviting feel
```

#### ネガティブプロンプト
```
realistic photography, 3D render, hyper-detailed feathers,
harsh lines, sharp edges, bold saturated colors, dark tones,
complex busy background, cluttered composition,
aggressive or dynamic pose, dramatic lighting,
modern digital art style, vector graphics, flat design,
overly simplified, too abstract, geometric shapes,
sad or angry expression, stiff or rigid pose,
photorealistic, detailed texture, professional photography
```

### 使用例

#### 例1: ふわふわコザクラインコ（基本）
```
Peach-faced lovebird fluffed up into round fluffy ball,
peachy pink face and chest, light green wings,
gentle expression with calm eyes, relaxed and cozy pose,

[共通テンプレートを適用]
```

#### 例2: 見つめるコザクラインコ
```
Peach-faced lovebird fluffed up, looking at viewer with curious eyes,
peachy pink and yellow coloring, soft green body,
tilted head pose, adorable and friendly expression,

[共通テンプレートを適用]
```

#### 例3: 複数のポーズ組み合わせ
```
Multiple poses of peach-faced lovebird in one image,
different angles: front view, side view, fluffed up ball,
peachy pink, yellow and green coloring,
variety of cute expressions and poses,

[共通テンプレートを適用]
```

#### 例4: セキセイインコ（応用例）
```
Budgerigar (parakeet) fluffed up into round fluffy ball,
light blue and white feather pattern,
gentle expression with calm eyes, relaxed and cozy pose,

[共通テンプレートを適用]
```

### Midjourney推奨パラメータ
```
--ar 1:1
--v 6
--stylize 400
--quality 2
```

### DALL-E 3推奨設定
```
Style: Illustration
Quality: Standard or HD
```

### Stable Diffusion推奨設定
```
Steps: 25-35
CFG Scale: 7-10
Sampler: DPM++ 2M Karras or Euler a
Model: Any illustration-focused model
```

---

## 今後追加予定のプリセット案

- **ミニマリスト商品写真**: 白背景、クリーンな照明、モダンな商品撮影
- **ファンタジーイラスト**: 幻想的な色彩、魔法的な雰囲気、RPG風
- **アーバンストリート**: 都市の夜景、ネオンライト、サイバーパンク風
- **ナチュラル&オーガニック**: アースカラー、自然光、植物や自然素材
- **ポップアートスタイル**: ビビッドカラー、グラフィック的、大胆な配色
- **水彩画風**: 柔らかい色のにじみ、透明感、アーティスティック

プリセットのリクエストがあれば、随時追加していきます!
