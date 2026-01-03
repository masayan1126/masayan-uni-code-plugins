# 画像生成AIプロンプトテクニック詳細

参考元: [実例付き]必ず押さえておきたい画像生成AIプロンプトテクニック6選
https://maasaablog.com/blog/qre8slp1v/

## 概要

このドキュメントでは、画像生成AIで高品質な画像を生成するための6つの実証済みテクニックを詳しく解説します。これらのテクニックを組み合わせることで、AI特有の「AI感」を軽減し、意図した通りの画像を生成できる確率が大幅に向上します。

---

## テクニック1: 優先順位

### 原則

**最も表現したい要素を冒頭に配置する**

AIは、プロンプトの最初の数語を最も強く認識し、画像生成の判断に大きく影響します。重要度の高い要素から順に記述することで、意図した被写体やメインテーマが正確に反映されます。

### 実践方法

#### ❌ 良くない例
```
high quality, 4K resolution, professional illustration,
beautiful landscape with mountains,
a woman standing in the foreground
```

問題点:
- 「高品質」「4K」などの品質指定が冒頭にある
- 実際のメインテーマ「女性」が最後に来ている
- AIは「高品質な風景」と解釈する可能性が高い

#### ✅ 良い例
```
a woman standing in the foreground,
beautiful landscape with mountains in the background,
high quality, 4K resolution, professional illustration
```

改善点:
- メインの被写体「女性」が冒頭にある
- 背景要素が次に来る
- 品質指定は最後に配置

### 優先順位の一般的な順序

```
1. メインの被写体（人物、オブジェクトなど）
2. 被写体の詳細（衣装、表情、ポーズなど）
3. 背景・環境（場所、時間帯、天候など）
4. スタイル・画風（アート様式、時代感など）
5. 色彩・照明（カラーパレット、光源など）
6. 雰囲気・ムード（感情、テーマなど）
7. 視点・構図（カメラアングル、フレーミングなど）
8. 品質・技術仕様（解像度、レンダリング方法など）
```

### 実例

**テーマ: ローファイ・ヒップホップのアルバムカバー**

❌ 優先順位が不明確:
```
lo-fi aesthetic, chill vibes, nostalgic,
retro anime style, 80s-90s,
high quality illustration,
Japanese woman with headphones
```

✅ 優先順位が明確:
```
Japanese woman with headphones,
relaxed posture, dreamy expression,
lo-fi aesthetic, nostalgic atmosphere,
retro anime style, 80s-90s Japanese animation,
high quality illustration
```

---

## テクニック2: 具体性

### 原則

**単語だけでなく、被写体やあらゆる箇所に詳細を加える**

曖昧な表現ではなく、具体的な描写を追加することで、AIが生成する画像の精度が向上し、「AI感」が軽減されます。

### 実践方法

#### レベル1: 基本（曖昧）
```
a cat
```

#### レベル2: 基本的な具体性
```
a gray tabby cat
```

#### レベル3: 詳細な具体性
```
a gray tabby cat with green eyes,
sitting by the window
```

#### レベル4: 高度な具体性
```
a gray tabby cat with bright green eyes and white paws,
sitting elegantly by the window sill,
basking in afternoon sunlight,
curious expression looking outside
```

### 具体性を高める要素

#### 人物の場合:
- **顔**: 表情、目の色、髪型、髪の色、肌の質感
- **体型**: スリム、がっしり、背の高さ
- **衣装**: スタイル、色、素材、ディテール
- **ポーズ**: 立っている、座っている、動作
- **感情**: 笑顔、真剣、リラックス

例:
```
a young Japanese woman with shoulder-length black hair,
wearing an oversized cream-colored hoodie,
relaxed posture sitting cross-legged,
gentle smile with eyes slightly closed,
headphones around her neck
```

#### 環境・背景の場合:
- **場所**: 室内/室外、具体的な場所
- **時間**: 朝、夕方、夜、季節
- **天候**: 晴れ、曇り、雨、雪
- **照明**: 自然光、人工光、特定の光源
- **雰囲気**: 静か、賑やか、神秘的

例:
```
cozy bedroom interior,
warm afternoon sunlight streaming through sheer curtains,
small potted plants on the windowsill,
soft ambient glow,
peaceful and quiet atmosphere
```

#### オブジェクトの場合:
- **形状**: 丸い、角ばった、有機的
- **素材**: 木、金属、ガラス、布
- **色**: 具体的な色名やカラーコード
- **質感**: 滑らか、粗い、光沢のある
- **状態**: 新品、使い古された、ヴィンテージ

例:
```
vintage vinyl record player,
wooden base with brass details,
glossy black turntable,
warm amber glow from the light,
well-maintained retro aesthetic
```

### 実例比較

**テーマ: 夜のカフェシーン**

❌ 具体性が低い:
```
person in cafe at night
```

✅ 具体性が高い:
```
young woman in her 20s sitting alone at corner table,
wearing casual knit sweater,
warm yellow cafe lights creating soft ambiance,
steam rising from coffee cup,
thoughtful expression gazing at laptop screen,
rain droplets visible on window behind her,
cozy urban cafe atmosphere at night
```

---

## テクニック3: 光源

### 原則

**AI感を抑えるために、かなり重要な要素**

光の方向、質、色温度を細かく指定することで、画像の立体感、雰囲気、リアリティが劇的に向上します。光源の指定は、プロの写真やイラストと「AI生成っぽさ」を分ける重要な要素です。

### 光源の3要素

#### 1. 光の種類
- **自然光**: 太陽光、月光、星明かり
- **人工光**: 蛍光灯、白熱灯、LED、ネオンサイン
- **環境光**: 反射光、間接照明、アンビエントライト
- **特殊光**: キャンドルライト、焚き火、スクリーンの光

#### 2. 光の方向
- **フロントライト**: 正面からの光
- **サイドライト**: 横からの光（立体感を強調）
- **バックライト/逆光**: 被写体の後ろからの光（シルエット効果）
- **トップライト**: 上からの光
- **ボトムライト**: 下からの光（ドラマチック効果）

#### 3. 光の質
- **ハードライト**: 硬い、鋭い影を作る直接光
- **ソフトライト**: 柔らかい、拡散した光
- **ディフューズライト**: 拡散光、間接光
- **スポットライト**: 特定の部分を照らす集中光

### 時間帯別の光の表現

#### ゴールデンアワー（日の出・日没前後）
```
warm golden hour light,
soft amber glow,
long shadows,
warm color temperature (2500-3500K),
diffused sunlight through atmosphere
```

#### 日中（正午前後）
```
bright midday sunlight,
strong overhead lighting,
short shadows,
neutral to cool color temperature (5500-6500K),
high contrast
```

#### ブルーアワー（日没後・日の出前）
```
cool blue twilight,
soft ambient glow,
gentle gradient sky,
cool color temperature (6500-8000K),
low contrast, ethereal atmosphere
```

#### 夜間
```
artificial city lights,
warm street lamps,
neon signs with vibrant colors,
stark contrast between light and shadow,
dramatic lighting
```

### 室内照明の表現

#### スタジオライト
```
professional studio lighting setup,
key light from 45-degree angle,
fill light for shadow control,
rim light for separation,
soft diffused quality
```

#### 自然な室内光
```
soft window light filtering through curtains,
diffused natural daylight,
gentle shadows,
warm ambient room lighting,
mixed color temperature
```

#### ムーディーな照明
```
single warm desk lamp,
concentrated pool of light,
deep shadows in background,
intimate atmosphere,
low-key lighting
```

### 実例

**テーマ: ポートレート写真**

❌ 光源の指定なし:
```
portrait of a woman,
professional photography
```

結果: フラットで立体感のない、AI特有の均一な照明

✅ 光源を詳細に指定:
```
portrait of a woman,
soft window light from left side at 45-degree angle,
natural diffused daylight,
gentle shadows defining facial contours,
warm color temperature (4000K),
professional photography
```

結果: 立体感があり、自然な光と影のあるプロフェッショナルな仕上がり

**テーマ: 夜のストリートシーン**

❌ 光源の指定が曖昧:
```
street at night,
city lights
```

✅ 光源を具体的に指定:
```
urban street at night,
warm sodium vapor street lamps casting orange glow,
neon signs in blue and pink creating color contrast,
wet pavement reflecting lights,
bokeh effect from distant city lights,
mixed warm and cool lighting,
cinematic noir atmosphere
```

---

## テクニック4: 視点

### 原則

**俯瞰、ズーム、ワイドなどカメラアングルを指定**

構図と視点を明確にすることで、意図した画像が生成されやすくなります。プロの写真やイラストでは、視点と構図が作品の印象を大きく左右します。

### カメラアングル（垂直方向）

#### アイレベル（目線の高さ）
```
eye-level shot,
neutral perspective,
natural viewer position
```

用途: 自然で親しみやすい、標準的な視点

#### ハイアングル（高い位置から）
```
high angle shot,
looking down at subject,
bird's eye view perspective
```

用途: 被写体を小さく見せる、全体像を把握

#### ローアングル（低い位置から）
```
low angle shot,
looking up at subject,
worm's eye view perspective
```

用途: 被写体を大きく、威圧的に見せる

#### 俯瞰（真上から）
```
top-down view,
overhead shot,
flat lay composition
```

用途: 配置やパターンを強調、デザイン的な構図

### カメラ距離（ショットサイズ）

#### エクストリームクローズアップ
```
extreme close-up,
macro shot,
focus on specific detail (e.g., eyes, hands)
```

#### クローズアップ
```
close-up shot,
face filling the frame,
intimate perspective
```

#### バストショット（胸から上）
```
bust shot,
head and shoulders,
medium close-up
```

#### ミディアムショット（腰から上）
```
medium shot,
waist up,
half body visible
```

#### フルショット（全身）
```
full body shot,
entire subject visible,
head to toe
```

#### ワイドショット
```
wide shot,
subject with significant environment,
establishing shot
```

#### エクストリームワイド
```
extreme wide shot,
vast landscape,
subject small in frame
```

### カメラアングル（水平方向）

#### フロント（正面）
```
frontal view,
straight-on angle,
facing camera directly
```

#### 3/4ビュー
```
three-quarter view,
slightly angled,
most common portrait angle
```

#### プロファイル（横顔）
```
profile view,
side angle,
90-degree turn
```

#### バックビュー（背面）
```
back view,
rear angle,
looking away from camera
```

### 構図テクニック

#### 三分割法
```
rule of thirds composition,
subject positioned at intersection points,
balanced arrangement
```

#### 中央配置
```
centered composition,
symmetrical arrangement,
subject in middle of frame
```

#### リーディングライン
```
leading lines composition,
lines guiding eye to subject,
perspective depth
```

#### フレーミング
```
natural framing,
subject framed by environmental elements,
layered composition
```

### 被写界深度

#### 浅い被写界深度
```
shallow depth of field,
blurred background (bokeh),
subject in sharp focus,
f/1.4 - f/2.8 aperture equivalent
```

用途: 被写体を強調、背景をぼかす

#### 深い被写界深度
```
deep depth of field,
everything in focus,
f/11 - f/22 aperture equivalent
```

用途: 風景、全体をシャープに

### 実例

**テーマ: キャラクターポートレート**

❌ 視点の指定なし:
```
portrait of a woman,
anime style
```

✅ 視点を詳細に指定:
```
portrait of a woman,
bust shot from slightly elevated angle,
three-quarter view with face turned 30 degrees,
shallow depth of field with soft bokeh background,
eye-level perspective creating intimate connection,
anime style
```

**テーマ: 商品写真**

❌ 視点が曖昧:
```
product photography,
coffee cup
```

✅ 視点を具体的に指定:
```
minimalist coffee cup,
top-down flat lay composition,
centered arrangement,
deep depth of field with everything in focus,
clean white background,
product photography style
```

---

## テクニック5: 画風

### 原則

**印象派、写実主義、ポップアート、浮世絵など様々なスタイルを指定可能**

著作権に配慮し、具体的な画家名より様式を説明することが推奨されます。画風の指定は、作品の芸術的方向性を決定する重要な要素です。

### 主要な画風カテゴリ

#### 1. 伝統的な西洋美術

**写実主義（Realism）**
```
realistic style,
photorealistic rendering,
accurate proportions and details,
true-to-life representation
```

**印象派（Impressionism）**
```
impressionist style,
visible brushstrokes,
emphasis on light and color,
loose and fluid composition
```

**表現主義（Expressionism）**
```
expressionist style,
bold colors and distorted forms,
emotional intensity,
dramatic representation
```

**キュビズム（Cubism）**
```
cubist style,
geometric shapes and fragmented forms,
multiple perspectives simultaneously,
abstract representation
```

**シュールレアリズム（Surrealism）**
```
surrealist style,
dreamlike and fantastical elements,
unexpected juxtapositions,
subconscious imagery
```

**ポップアート（Pop Art）**
```
pop art style,
bold colors and flat shapes,
commercial imagery aesthetic,
graphic design influence
```

#### 2. アジアの伝統美術

**浮世絵（Japanese Woodblock Print）**
```
ukiyo-e style,
Japanese woodblock print aesthetic,
flat colors with clear outlines,
traditional Japanese composition
```

**水墨画（Ink Wash Painting）**
```
sumi-e style,
monochrome ink wash technique,
minimalist with emphasis on empty space,
flowing brushwork
```

**中国画（Chinese Painting）**
```
traditional Chinese painting style,
delicate brushwork,
harmonious composition with nature,
subtle color palette
```

#### 3. 現代・デジタルアート

**アニメ・マンガスタイル**
```
anime style,
clean linework,
cel-shaded coloring,
expressive eyes and features

manga style,
black and white with screentone,
dynamic composition,
speed lines and effects
```

**時代別アニメスタイル**

1970-80年代:
```
retro 70s-80s anime style,
detailed linework,
muted color palette,
classic Japanese animation aesthetic
```

1990年代:
```
90s anime style,
vibrant colors,
detailed backgrounds,
cel animation aesthetic
```

2000年代以降:
```
modern anime style,
clean digital coloring,
sharp lines,
contemporary Japanese animation
```

**デジタルアート**
```
digital art style,
clean digital rendering,
gradient shading,
modern illustration technique
```

**ピクセルアート**
```
pixel art style,
8-bit or 16-bit aesthetic,
retro game graphics,
limited color palette
```

**ローポリ3D**
```
low-poly 3D style,
geometric polygonal shapes,
minimalist 3D rendering,
flat colors
```

#### 4. 特殊なスタイル

**ノワール（Film Noir）**
```
film noir style,
high contrast black and white,
dramatic shadows,
moody and mysterious atmosphere
```

**ヴィンテージ**
```
vintage style,
aged and weathered appearance,
retro color grading,
nostalgic aesthetic
```

**ミニマリスト**
```
minimalist style,
simple forms and limited colors,
emphasis on negative space,
clean and uncluttered
```

**グランジ**
```
grunge style,
rough textures and distressed elements,
gritty and raw aesthetic,
urban decay influence
```

### 画風の組み合わせ

複数のスタイルを組み合わせることで、ユニークな表現が可能:

```
retro anime style with impressionist influence,
soft brushstroke-like textures,
vibrant color palette,
nostalgic 80s Japanese animation aesthetic
with dreamy, painted quality
```

### 著作権への配慮

#### ❌ 避けるべき表現
```
in the style of [specific artist name]
like [artist name]'s work
resembling [copyrighted character]
```

#### ✅ 推奨される表現
```
impressionist style
90s anime aesthetic
retro game art style
contemporary digital illustration
```

### 実例

**テーマ: ローファイ・ヒップホップアルバムカバー**

❌ 画風が曖昧:
```
illustration of woman with headphones,
retro style
```

✅ 画風を具体的に指定:
```
illustration of woman with headphones,
retro anime style reminiscent of 80s-90s Japanese animation,
cel-shaded coloring with soft gradients,
nostalgic aesthetic with warm vintage color grading,
clean linework with subtle grain texture,
lo-fi animation quality
```

**テーマ: 商品パッケージデザイン**

❌ 画風の指定なし:
```
coffee package design
```

✅ 画風を明確に指定:
```
coffee package design,
minimalist Scandinavian design style,
clean geometric shapes,
limited color palette with earth tones,
contemporary branding aesthetic,
professional product design
```

---

## テクニック6: 色調・色彩

### 原則

**アースカラーやラグジュアリーカラーなど、色パレットを指定することで作品の雰囲気を統制できる**

色彩は画像の印象を決定づける最も直接的な要素です。色の選択、組み合わせ、配分を明確にすることで、意図した雰囲気やブランドイメージを正確に表現できます。

### 色指定の方法

#### 1. 色名での指定
```
warm red, deep blue, soft pastel pink
```

#### 2. カラーコードでの指定（最も正確）
```
deep blue (#2641C0),
vibrant red (#E52436),
off-white (#F5F5F5)
```

#### 3. カラーパレット名での指定
```
earth tone palette,
pastel color scheme,
monochromatic blue palette
```

### 代表的なカラーパレット

#### アースカラー（Earth Tones）
```
earth tone color palette:
- warm browns (#8B6F47)
- terracotta (#CD5C5C)
- sage green (#9CA777)
- sand beige (#E8D5B7)
- natural and organic feel
```

用途: 自然、オーガニック、落ち着いた雰囲気

#### パステルカラー（Pastel Colors）
```
pastel color palette:
- soft pink (#FFB3BA)
- mint green (#BAE1BA)
- baby blue (#BFEFFF)
- lavender (#D4A5A5)
- gentle and dreamy atmosphere
```

用途: 可愛らしい、優しい、夢のような雰囲気

#### ビビッドカラー（Vivid Colors）
```
vivid color palette:
- electric blue (#00BFFF)
- hot pink (#FF69B4)
- bright yellow (#FFD700)
- vibrant purple (#9370DB)
- energetic and bold
```

用途: エネルギッシュ、若々しい、インパクトのある

#### モノクロマティック（Monochromatic）
```
monochromatic blue palette:
- deep navy (#001F3F)
- medium blue (#0074D9)
- sky blue (#7FDBFF)
- ice blue (#E0F2F7)
- harmonious and cohesive
```

用途: 統一感、洗練された、ミニマリスト

#### ラグジュアリーカラー（Luxury Colors）
```
luxury color palette:
- deep burgundy (#800020)
- rich gold (#FFD700)
- midnight blue (#191970)
- cream white (#FFFDD0)
- sophisticated and premium feel
```

用途: 高級感、エレガント、プレミアム

#### サイバーパンク（Cyberpunk）
```
cyberpunk color palette:
- neon pink (#FF10F0)
- electric cyan (#00F0FF)
- deep purple (#2D1B69)
- dark background (#0A0E27)
- futuristic and dystopian
```

用途: 未来的、テクノロジー、ネオン街

#### レトロ/ヴィンテージ（Retro/Vintage）
```
retro 80s color palette:
- sunset orange (#FF6B35)
- teal (#008B8B)
- dusty pink (#D4A5A5)
- cream yellow (#FFFACD)
- nostalgic 80s vibe
```

用途: ノスタルジック、レトロ、ヴィンテージ

### 色の役割と配分

#### ベースカラー（60%）
主要な背景色や大部分を占める色
```
base color: soft off-white (#F5F5F5)
covering majority of the composition
```

#### メインカラー（30%）
作品の主要な印象を決める色
```
main color: deep blue (#2641C0)
primary accent and focal point
```

#### アクセントカラー（10%）
視線を引き付ける強調色
```
accent color: vibrant red (#E52436)
small pops of color for emphasis
```

### 色温度（Color Temperature）

#### 暖色系（Warm Colors）
```
warm color temperature:
reds, oranges, yellows,
cozy and inviting atmosphere,
emotional warmth
```

#### 寒色系（Cool Colors）
```
cool color temperature:
blues, greens, purples,
calm and serene atmosphere,
professional and clean feel
```

#### ニュートラル（Neutral）
```
neutral color temperature:
balanced warm and cool tones,
versatile and timeless
```

### 色の対比とハーモニー

#### 補色（Complementary）
```
complementary colors:
blue (#0000FF) and orange (#FFA500),
high contrast and vibrant,
dynamic visual impact
```

#### 類似色（Analogous）
```
analogous colors:
blue, blue-green, green,
harmonious and pleasing,
smooth color transition
```

#### トライアド（Triadic）
```
triadic colors:
red, yellow, blue (primary colors),
balanced and vibrant,
rich color diversity
```

### 色の心理効果

#### 赤（Red）
```
red tones:
energy, passion, urgency,
attention-grabbing
```

#### 青（Blue）
```
blue tones:
trust, calm, professionalism,
stability and serenity
```

#### 緑（Green）
```
green tones:
nature, growth, harmony,
fresh and peaceful
```

#### 黄色（Yellow）
```
yellow tones:
happiness, optimism, energy,
cheerful and bright
```

#### 紫（Purple）
```
purple tones:
luxury, creativity, mystery,
sophisticated and unique
```

### 実例

**テーマ: ローファイ・ヒップホップアルバムカバー**

❌ 色指定が曖昧:
```
colorful illustration,
retro colors
```

✅ 色彩を詳細に指定:
```
color palette:
- base: deep navy blue (#2641C0) - 60%
- accent: warm sunset red (#E52436) - 30%
- highlights: soft cream (#F5E6D3) - 10%

overall warm color temperature,
nostalgic retro color grading,
slightly desaturated for vintage feel,
smooth gradient transitions between colors
```

**テーマ: ミニマリスト商品写真**

❌ 色の指定なし:
```
product photography,
minimalist style
```

✅ 色彩を明確に指定:
```
minimalist product photography,
monochromatic neutral palette:
- soft off-white (#F5F5F5) background
- charcoal gray (#2C2C2C) product
- subtle warm highlights (#E8DED2)

cool color temperature (6000K),
low saturation for sophisticated feel,
clean and understated color scheme
```

**テーマ: ファンタジーイラスト**

❌ 色が曖昧:
```
fantasy illustration,
magical colors
```

✅ 色彩を具体的に指定:
```
fantasy illustration,
ethereal color palette:
- deep twilight purple (#4A0E4E) - shadows
- magical pink (#FF69B4) - highlights
- soft lavender (#D4A5D4) - midtones
- shimmering gold (#FFD700) - accents

color palette with high saturation,
glowing luminescent effects,
complementary purple-gold contrast,
dreamlike and mystical atmosphere
```

---

## 6つのテクニックを統合した実例

### 実例1: ローファイ・ヒップホップアルバムカバー

**完全版プロンプト:**

```
Japanese woman in her 20s with shoulder-length black hair,
wearing oversized vintage cream hoodie and knit beanie,
relaxed cross-legged posture with wireless headphones around neck,
gentle smile with eyes slightly closed in contentment,
sitting by large window with small potted plants on sill,

color palette:
deep navy blue (#2641C0) base with warm sunset red (#E52436) accents,
soft cream (#F5E6D3) highlights,
slightly desaturated for nostalgic feel,

retro anime style reminiscent of 80s-90s Japanese animation,
cel-shaded coloring with soft gradients and subtle grain texture,
lo-fi aesthetic,

warm afternoon golden hour light streaming through window,
soft diffused sunlight at 45-degree angle from left,
warm color temperature (3500K) creating cozy atmosphere,

medium shot from slightly elevated angle,
three-quarter view,
shallow depth of field with soft bokeh background,

nostalgic and chill atmosphere,
lo-fi hip-hop vibe,
peaceful and introspective mood,

highly detailed, professional digital illustration
```

**ネガティブプロンプト:**
```
hyper-realistic, 3D render, modern digital art style,
harsh fluorescent lighting, overly saturated colors,
busy cluttered background, too many details,
photorealistic skin texture, CGI appearance
```

### 実例2: ミニマリスト商品写真

**完全版プロンプト:**

```
minimalist ceramic coffee mug with clean geometric lines,
smooth matte white (#F5F5F5) finish with subtle texture,
simple cylindrical form with gently curved handle,
placed on natural marble surface with soft gray veining,

monochromatic neutral palette:
off-white (#F5F5F5) primary,
charcoal gray (#2C2C2C) shadows,
warm cream (#E8DED2) subtle highlights,
cool color temperature (6000K),

contemporary Scandinavian design aesthetic,
minimalist product photography style,
clean and sophisticated,

soft diffused studio lighting from 45-degree angle,
key light with fill light for shadow control,
gentle shadows defining form,
even ambient illumination,

top-down view with slight angle,
centered composition following rule of thirds,
deep depth of field with entire product in sharp focus,

serene and premium atmosphere,
understated luxury feel,
calm and professional mood,

ultra high resolution, 8K quality,
photorealistic rendering with perfect focus
```

**ネガティブプロンプト:**
```
cluttered background, busy patterns,
overly dramatic lighting, harsh shadows,
vintage or distressed appearance,
warm color tones, vibrant colors,
artificial bokeh effects, lens flares
```

---

## まとめ: 6つのテクニックチェックリスト

プロンプトを作成する際は、以下のチェックリストを確認してください:

- [ ] **優先順位**: 最も重要な要素が冒頭にあるか?
- [ ] **具体性**: 各要素に十分な詳細が含まれているか?
- [ ] **光源**: 光の種類、方向、質が明確に指定されているか?
- [ ] **視点**: カメラアングル、距離、構図が定義されているか?
- [ ] **画風**: スタイルや様式が具体的に記述されているか?
- [ ] **色彩**: 色パレット、カラーコード、配分が明確か?

これら6つの要素を全て考慮することで、AI感を最小限に抑え、プロフェッショナルな品質の画像生成が可能になります。
