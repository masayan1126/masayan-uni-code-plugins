# Design Guidelines

## デザイン思考

コーディング前に、コンテキストを理解し大胆な美的方向性にコミットする。

### 理解すべきポイント

- **目的**: このプレゼンはどんな問題を解決するか？誰が見るか？
- **トーン**: 極端な方向性を選ぶ
- **差別化**: 何がこのスライドを忘れられなくするか？

### トーンの選択肢

| トーン | 特徴 |
|--------|------|
| Brutally Minimal | 極限まで削ぎ落とした余白と要素 |
| Maximalist Chaos | 情報過多を意図的にデザイン化 |
| Retro-Futuristic | レトロとSFの融合 |
| Organic/Natural | 自然物の曲線と温かみ |
| Luxury/Refined | 高級感と洗練 |
| Playful/Toy-like | おもちゃのような楽しさ |
| Editorial/Magazine | 雑誌のようなレイアウト |
| Brutalist/Raw | 生々しい素材感 |
| Art Deco/Geometric | 幾何学パターンとアールデコ |
| Soft/Pastel | 柔らかい色調 |
| Industrial/Utilitarian | 工業的・機能的 |
| Neon/Cyberpunk | ネオンと暗闘のコントラスト |

## タイポグラフィ

### 避けるべきフォント

- Inter, Roboto, Arial, system fonts
- 汎用的すぎるフォント

### 推奨アプローチ

- **ディスプレイフォント**: 見出し用に個性的なフォント
- **ボディフォント**: 本文用に読みやすい洗練されたフォント
- **フォントペアリング**: ディスプレイ + ボディの組み合わせ

### Slidevでのフォント設定

```yaml
# frontmatter
fonts:
  sans: 'Noto Sans JP'
  serif: 'Noto Serif JP'
  mono: 'Fira Code'
  provider: 'google'
```

## カラー & テーマ

### 原則

- 支配的な色と鋭いアクセントを使う
- 均等に分散した臆病なパレットは避ける
- CSS変数で一貫性を保つ

### Slidevでのカスタムスタイル

```css
/* style.css */
:root {
  --slidev-theme-primary: #FF6B35;
  --slidev-theme-secondary: #004E64;
  --slidev-theme-background: #0A0A0A;
  --slidev-theme-text: #FFFFFF;
}
```

### カラーパレット例

| テーマ | Primary | Secondary | Background | Text |
|--------|---------|-----------|------------|------|
| Neon Night | #00FF88 | #FF00AA | #0D0D0D | #FFFFFF |
| Earth Tone | #8B4513 | #228B22 | #F5F5DC | #2F4F4F |
| Corporate Bold | #FF6B35 | #004E64 | #FFFFFF | #1A1A1A |
| Pastel Dream | #FFB6C1 | #87CEEB | #FFF5EE | #4A4A4A |

## モーション

### アニメーション方針

- 高インパクトな瞬間に集中
- ページロード時のスタガードアニメーション
- ホバー・クリック時の驚き

### Slidevでのトランジション

```yaml
# frontmatter
transition: slide-left
```

### 使用可能なトランジション

- `slide-left`, `slide-right`, `slide-up`, `slide-down`
- `fade`, `fade-out`
- `view-transition`

### スライド内アニメーション（v-click）

```md
<v-clicks>

- 最初に表示
- 次にクリックで表示
- さらにクリックで表示

</v-clicks>
```

## 空間構成

### レイアウト原則

- 予想外のレイアウト
- 非対称性
- オーバーラップ
- 対角線フロー
- グリッドを意図的に破る要素
- 余白を大胆に使う OR 密度をコントロール

### Slidevレイアウト例

```md
---
layout: two-cols
---

# 左カラム

::right::

# 右カラム
```

## 背景 & ビジュアル詳細

### 避けるべきもの

- 単色の白・グレー背景のみ
- **グラデーション全般（絶対禁止）** - AI生成の典型的なデザインであり、安っぽく見える
  - linear-gradient, radial-gradient など全て禁止
  - 紫グラデーションは特に避ける

### 推奨エフェクト

- ノイズテクスチャ
- 幾何学パターン
- レイヤード透過
- ドラマチックなシャドウ
- 装飾的ボーダー

### Slidevでの背景設定

```md
---
background: /path/to/image.jpg
class: 'text-center'
---
```

```md
---
background: '#0A0A0A'
class: 'bg-[url("/noise.png")] bg-repeat'
---
```

## アイコン

### 基本方針

- **積極的にアイコンを使用する** - 視覚的インパクトと理解しやすさを向上
- テキストだけのスライドは避け、アイコンで補強する
- 見出し、リスト項目、概念図にアイコンを添える

### Slidevでのアイコン使用（UnoCSS Icons）

SlidevはUnoCSS Iconsを標準サポート。Iconifyの全アイコンセットが使用可能。

```md
<!-- 基本構文: <{collection}-{icon-name} /> -->
<carbon-rocket class="text-4xl text-blue-500"/>
<mdi-lightbulb class="text-3xl text-yellow-400"/>
<ph-code-bold class="text-2xl"/>
```

### 推奨アイコンセット

| セット | プレフィックス | 特徴 | 用途 |
|--------|---------------|------|------|
| Carbon | `carbon-` | IBMデザイン、モダン | テック系、ビジネス |
| Material Design | `mdi-` | 豊富な種類 | 汎用 |
| Phosphor | `ph-` | 美しい線画 | 洗練されたデザイン |
| Heroicons | `heroicons-` | Tailwind公式 | モダンUI |
| Lucide | `lucide-` | Featherの後継 | ミニマル |
| Tabler | `tabler-` | 線幅統一 | 技術文書 |
| Simple Icons | `simple-icons-` | ブランドロゴ | 企業・サービス紹介 |
| Logos | `logos-` | 開発ツールロゴ | 技術スタック紹介 |

### アイコン活用パターン

#### 見出しにアイコン

```md
# <carbon-rocket class="inline-block"/> はじめに
```

#### リスト項目にアイコン

```md
- <mdi-check-circle class="text-green-500"/> 完了した機能
- <mdi-clock class="text-yellow-500"/> 進行中
- <mdi-close-circle class="text-red-500"/> 未着手
```

#### 技術スタック紹介

```md
<div class="flex gap-8 text-6xl">
  <logos-vue />
  <logos-typescript-icon />
  <logos-tailwindcss-icon />
  <logos-github-icon />
</div>
```

#### アイコン付きカード

```md
<div class="grid grid-cols-3 gap-4">
  <div class="p-4 bg-blue-500/10 rounded-lg text-center">
    <carbon-analytics class="text-5xl text-blue-500 mx-auto"/>
    <p class="mt-2 font-bold">分析</p>
  </div>
  <div class="p-4 bg-green-500/10 rounded-lg text-center">
    <carbon-growth class="text-5xl text-green-500 mx-auto"/>
    <p class="mt-2 font-bold">成長</p>
  </div>
  <div class="p-4 bg-purple-500/10 rounded-lg text-center">
    <carbon-idea class="text-5xl text-purple-500 mx-auto"/>
    <p class="mt-2 font-bold">革新</p>
  </div>
</div>
```

#### フロー図（アイコン + 矢印）

```md
<div class="flex items-center justify-center gap-4 text-4xl">
  <carbon-document />
  <carbon-arrow-right class="text-gray-400"/>
  <carbon-ai />
  <carbon-arrow-right class="text-gray-400"/>
  <carbon-checkmark-filled class="text-green-500"/>
</div>
```

### アイコンスタイリング

```md
<!-- サイズ -->
<carbon-star class="text-sm"/>   <!-- 小 -->
<carbon-star class="text-2xl"/>  <!-- 中 -->
<carbon-star class="text-6xl"/>  <!-- 大 -->

<!-- 色 -->
<carbon-star class="text-red-500"/>
<carbon-star class="text-[#FF6B35]"/>

<!-- アニメーション -->
<carbon-rotate class="animate-spin"/>
<carbon-arrow-down class="animate-bounce"/>

<!-- ホバー効果 -->
<carbon-star class="hover:text-yellow-400 transition-colors"/>
```

### よく使うアイコン例

| 用途 | アイコン例 |
|------|-----------|
| 開始・導入 | `carbon-rocket`, `carbon-play-filled` |
| アイデア | `carbon-idea`, `mdi-lightbulb` |
| 設定・ツール | `carbon-settings`, `carbon-tools` |
| コード | `carbon-code`, `ph-code-bold` |
| データ | `carbon-analytics`, `carbon-chart-line` |
| 成功 | `carbon-checkmark-filled`, `mdi-check-circle` |
| 警告 | `carbon-warning`, `mdi-alert` |
| 時間 | `carbon-time`, `mdi-clock` |
| ユーザー | `carbon-user`, `carbon-user-multiple` |
| 矢印 | `carbon-arrow-right`, `carbon-arrow-down` |

## スライドの情報量とレイアウト品質

### 情報量の原則

- **1スライド = 1メッセージ**: 伝えたいことを1つに絞る
- 箇条書きは **最大5〜6項目** を目安。超える場合はスライドを分割
- コードブロックは **15行以内** に収める。長い場合はハイライト行を絞るか分割
- テーブルは **5行×4列程度** まで。大きいテーブルは分割 or 要約

### 縦方向バジェット（見切れ防止の根本ルール）

Slidevの表示領域は **960×540px**。defaultレイアウトの上下パディングを除くと、コンテンツに使える縦方向は **約456px**。全要素の高さ合計がこれを超えると下部が見切れる。

**概算の高さ参照テーブル**:

| 要素 | 概算の高さ |
|------|-----------|
| h1見出し + 説明テキスト | 60〜80px |
| ターミナルブロック（1行あたり） | 約18px/行 + 装飾40px |
| カード（padding 0.8rem） | 約60px |
| カード（padding 1.2rem） | 約85px |
| v-clickカード | 約50px + margin |
| gap/margin（mt-3） | 12px |

**ターミナルブロックの必須ルール**:
- **装飾目的の空行（`<br/>`）は禁止** — ボックスアートのpadding行、コマンド間の空行を入れない
- ターミナル単体は **最大8行**、下部にカード等がある場合は **最大6行**
- `.terminal` CSS: `padding: 0.7rem 1.2rem`、`font-size: 0.75rem`、`line-height: 1.5`、**`white-space: pre`（必須 — これがないとHTMLの空白結合でインデントが消える）**
- `::before` は `margin-bottom: 0.5rem`、`padding-bottom: 0.4rem` 以下

**ターミナル + 下部要素の組み合わせ制限**:
- 6行以下 → カード3枚(3列) or カード2枚(2列)+v-click1枚
- 7〜8行 → v-clickカード1枚のみ
- 9行以上 → ターミナルだけでスライド1枚

### レイアウト品質チェック

- **配置バランス**:
  - 要素が片側に偏らないようにする
  - `two-cols` レイアウト使用時は左右のボリュームを揃える
  - グリッド配置ではアイテム数が行に均等に並ぶよう調整
- **フォントサイズの適切な選択**:
  - 見出し: `text-2xl` 〜 `text-4xl`（カバーは `text-5xl` まで可）
  - 本文: `text-base` 〜 `text-lg`
  - 補足: `text-sm`（`text-xs` は最終手段）
  - 情報を小さくして詰め込むくらいなら、スライドを分割する

## 重要な注意

- **実装の複雑さはビジョンに合わせる**
  - マキシマリストデザイン → 精緻なコードとエフェクト
  - ミニマリストデザイン → 節制、精密、繊細なディテール
- **同じデザインを繰り返さない**
  - 毎回異なるテーマ・フォント・美学
- **大胆にコミットする**
  - 中途半端な方向性は避け、選んだ美学を徹底する
