# 画像生成AIプロンプトテクニック詳細

参考元: [実例付き]必ず押さえておきたい画像生成AIプロンプトテクニック6選
https://maasaablog.com/blog/qre8slp1v/

## テクニック1: 優先順位

**最も表現したい要素を冒頭に配置**

```
# 良くない例
high quality, 4K, professional illustration, a woman

# 良い例
a woman, beautiful landscape, high quality, 4K
```

### 一般的な順序
1. メインの被写体
2. 被写体の詳細
3. 背景・環境
4. スタイル・画風
5. 色彩・照明
6. 雰囲気
7. 視点・構図
8. 品質・技術仕様

---

## テクニック2: 具体性

**単語だけでなく詳細な説明を追加**

| レベル | 例 |
|--------|-----|
| 基本 | a cat |
| 詳細 | a gray tabby cat |
| 高度 | a gray tabby cat with green eyes, sitting by the window |

### 具体性を高める要素

**人物**: 表情、髪型、衣装、ポーズ、感情
**環境**: 場所、時間、天候、照明、雰囲気
**オブジェクト**: 形状、素材、色、質感、状態

---

## テクニック3: 光源

**AI感を抑える重要な要素**

### 光源の3要素
- **種類**: 自然光/人工光/環境光/特殊光
- **方向**: フロント/サイド/バック/トップ
- **質**: ハード/ソフト/ディフューズ

### 時間帯別の表現

```yaml
ゴールデンアワー: warm golden hour light, soft amber glow
日中: bright midday sunlight, high contrast
ブルーアワー: cool blue twilight, ethereal atmosphere
夜間: artificial city lights, dramatic lighting
```

---

## テクニック4: 視点

### カメラアングル（垂直）
- **アイレベル**: neutral perspective
- **ハイアングル**: looking down, bird's eye view
- **ローアングル**: looking up, worm's eye view
- **俯瞰**: top-down view, flat lay

### ショットサイズ
- **クローズアップ**: face filling the frame
- **バストショット**: head and shoulders
- **ミディアム**: waist up
- **フルショット**: entire subject visible
- **ワイド**: subject with significant environment

### 被写界深度
- **浅い**: blurred background (bokeh), f/1.4-2.8
- **深い**: everything in focus, f/11-22

---

## テクニック5: 画風

### 伝統的美術
- **写実主義**: photorealistic rendering
- **印象派**: visible brushstrokes, emphasis on light
- **ポップアート**: bold colors, flat shapes

### アジア美術
- **浮世絵**: ukiyo-e style, flat colors with clear outlines
- **水墨画**: sumi-e style, monochrome ink wash

### 現代・デジタル
- **アニメ**: anime style, cel-shaded coloring
- **ピクセルアート**: 8-bit aesthetic
- **ローポリ3D**: geometric polygonal shapes

### 時代別アニメスタイル
```yaml
1970-80年代: retro 70s-80s anime, muted palette
1990年代: 90s anime, vibrant colors, cel animation
2000年代〜: modern anime, clean digital coloring
```

---

## テクニック6: 色調・色彩

### カラーパレット例

| パレット | 色例 | 用途 |
|----------|------|------|
| アースカラー | #8B6F47, #CD5C5C | 自然、落ち着いた |
| パステル | #FFB3BA, #BAE1BA | 優しい、夢のような |
| ビビッド | #00BFFF, #FF69B4 | エネルギッシュ |
| サイバーパンク | #FF10F0, #00F0FF | 未来的 |
| レトロ80s | #FF6B35, #008B8B | ノスタルジック |

### 色の役割と配分
- **ベース（60%）**: 主要な背景色
- **メイン（30%）**: 主要な印象を決める色
- **アクセント（10%）**: 視線を引く強調色

---

## 統合実例

```
Japanese woman with headphones,
relaxed posture, dreamy expression,
color palette: deep navy (#2641C0) base, red (#E52436) accents,
retro anime style, 80s-90s aesthetic,
warm golden hour light from left,
bust shot, three-quarter view, shallow depth of field,
nostalgic lo-fi atmosphere,
high quality digital illustration

Negative prompt: hyper-realistic, 3D render, harsh lighting
```
