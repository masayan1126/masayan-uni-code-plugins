# プロンプトテンプレート

## 基本構造

```
【主題・被写体】
- メインキャラクター/オブジェクト: [詳細な説明]
- 衣装・アクセサリー: [具体的な特徴]
- ポーズ・表情: [動きや感情]

【色彩・カラーパレット】
- ベースカラー: [色名/カラーコード]
- アクセントカラー: [色名/カラーコード]
- 全体のトーン: [明度・彩度の特徴]

【スタイル・画風】
- 芸術様式: [具体的なスタイル]
- 時代感・ジャンル: [参考となる年代や分野]

【雰囲気・効果】
- ムード: [感情や雰囲気]
- テーマ: [コンセプト]

【光源・照明】（オプション）
- 光の種類・方向・質

【視点・構図】（オプション）
- カメラアングル・フレーミング

【技術仕様】（オプション）
- 解像度・レンダリング

【ネガティブプロンプト】（オプション）
- 避けるべき要素
```

---

## 実行用プロンプト形式

```
[最優先の被写体], [詳細な特徴],
[色彩指定: ベースカラー, アクセントカラー],
[スタイル・画風], [雰囲気・ムード],
[光源・照明], [視点・構図],
[品質・技術仕様]

Negative prompt: [避けたい要素]
```

---

## 例1: ローファイ・ヒップホップ

```
Japanese woman with headphones,
wearing oversized vintage hoodie,
relaxed cross-legged posture, dreamy expression,
color palette: deep navy (#2641C0) base, red (#E52436) accents,
retro anime style, 80s-90s aesthetic, cel-shaded,
lo-fi hip-hop atmosphere, nostalgic mood,
warm golden hour light, soft diffused from left,
bust shot, three-quarter view, shallow depth of field,
high quality digital illustration

Negative prompt: hyper-realistic, 3D render, modern style, harsh lighting
```

---

## 例2: ミニマリスト商品

```
minimalist ceramic coffee mug,
clean geometric lines, matte white finish,
on natural marble surface,
monochromatic palette: off-white (#F5F5F5), charcoal (#2C2C2C),
contemporary Scandinavian design,
soft studio lighting from 45-degree angle,
top-down with slight angle, deep depth of field,
ultra high resolution, photorealistic

Negative prompt: cluttered background, dramatic shadows, vintage style
```

---

## 例3: ゆるふわインコ

```
Peach-faced lovebird fluffed up into round ball,
peachy pink face, light green wings,
gentle calm expression, relaxed cozy pose,
soft pastel colors (#FFE5D9, #FFF9C4, #C8E6C9),
hand-drawn style, watercolor texture,
kawaii yurufuwa aesthetic,
soft natural lighting, minimal shadows,
centered on white background,
healing heartwarming atmosphere

Negative prompt: realistic photography, harsh lines, dark tones
```

---

## ヒアリング質問

### 必須
1. **主題・被写体**: メインの対象と具体的特徴
2. **色彩**: 使用したい色やカラーコード
3. **スタイル**: 希望する画風
4. **雰囲気**: 表現したい感情やテーマ

### オプション
5. **光源**: 光の質や方向
6. **視点**: カメラアングルや構図
7. **品質**: 技術要件
8. **ネガティブ**: 避けたい要素

---

## クリップボードコピー

生成後、以下の選択肢を提示:
1. ポジティブプロンプトのみ（推奨）
2. ネガティブプロンプトのみ
3. 両方（統合）
4. コピーしない
