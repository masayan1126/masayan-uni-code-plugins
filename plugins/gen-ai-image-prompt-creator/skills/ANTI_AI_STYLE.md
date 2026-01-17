# AIっぽさ緩和オプション

画像生成AIで作成した画像の「AIっぽさ」を軽減するための推奨オプション。

## 確認項目

プロンプト生成前に、以下の2つのオプションを含めるかユーザーに確認すること：

| オプション | プロンプト追加文 | 効果 |
|-----------|-----------------|------|
| **ベタ塗り** | `flat colors`, `solid color fills`, `no gradients` | グラデーション過多を抑制 |
| **デフォルメされたフォルム** | `stylized proportions`, `deformed cute form`, `chibi-like proportions` | 過度にリアルな造形を回避 |

## 確認フロー

```
AskUserQuestion で以下を確認:

「AIっぽさを軽減するオプションを適用しますか？」

選択肢:
- 両方適用（推奨）: ベタ塗り＋デフォルメ
- ベタ塗り
- デフォルメされたフォルム
- 適用しない
```

## 適用例

**適用前:**
```
cute parrot character, soft lighting, detailed feathers
```

**適用後（両方）:**
```
cute parrot character, soft lighting, detailed feathers, flat colors, solid color fills, stylized proportions, deformed cute form
```

## 注意事項

- 写実的なスタイルを希望する場合は「適用しない」を選択
- 技術図解やダイアグラム系は「ベタ塗り」のみ推奨
- キャラクター・マスコット系は「両方適用」推奨
