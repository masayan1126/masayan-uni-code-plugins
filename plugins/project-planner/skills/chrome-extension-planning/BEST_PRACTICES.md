# ベストプラクティス

このドキュメントでは、Chrome拡張機能企画を成功させるためのベストプラクティスと実践的なガイドラインを提供します。

## 企画の原則

### Manifest V3準拠

Chrome拡張機能は2024年以降、Manifest V3が必須となっています：

- Service Workerベースのバックグラウンド処理
- declarativeNetRequestによるネットワーク制御
- コンテンツセキュリティポリシーの厳格化
- リモートコードの実行禁止

```json
// Manifest V3の基本構造
{
  "manifest_version": 3,
  "background": {
    "service_worker": "background.js"
  }
}
```

### 最小権限の原則

ユーザーの信頼を得るため、必要最小限の権限のみを要求：

#### やるべきこと
- 使用する機能に対応する権限のみ要求
- optional_permissionsを活用（必要時に権限要求）
- host_permissionsは必要なドメインのみに限定
- 権限が必要な理由をストア説明文に明記

#### 避けるべきこと
- `<all_urls>`の安易な使用
- 未使用のAPIに対する権限要求
- 説明なしの広範な権限要求
- activeTabで代替可能な場合のtabs権限

```json
// 良い例: 必要最小限の権限
{
  "permissions": ["storage", "activeTab"],
  "optional_permissions": ["notifications"],
  "host_permissions": ["https://specific-site.com/*"]
}

// 避けるべき例: 過剰な権限
{
  "permissions": ["tabs", "storage", "notifications", "cookies"],
  "host_permissions": ["<all_urls>"]
}
```

### プライバシー重視

#### やるべきこと
- ユーザーデータの収集は最小限に
- プライバシーポリシーを明確に記載
- データの保存場所と用途を説明
- GDPRやCCPAへの対応を考慮

#### 避けるべきこと
- 不必要なデータ収集
- 外部への無断送信
- 曖昧なプライバシーポリシー
- ユーザー追跡機能の隠蔽

## 技術的なベストプラクティス

### Service Worker設計

```javascript
// 良い例: イベントドリブンで効率的
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete') {
    // 処理
  }
});

// 良い例: アラームの適切な使用
chrome.alarms.create('periodicTask', { periodInMinutes: 30 });
chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === 'periodicTask') {
    // 定期処理
  }
});
```

**注意点:**
- Service Workerは30秒でタイムアウトする可能性あり
- 長時間実行される処理は避ける
- 状態はchrome.storageに保存（メモリは永続化されない）

### ストレージ設計

```javascript
// chrome.storage.sync: 同期データ（100KB上限、アイテムあたり8KB）
// 設定、ユーザー preferences
chrome.storage.sync.set({ settings: { theme: 'dark' } });

// chrome.storage.local: ローカルデータ（5MB上限、unlimitedStorageで無制限）
// キャッシュ、大量データ
chrome.storage.local.set({ cache: largeData });

// セッションストレージ: 一時データ（Manifest V3）
chrome.storage.session.set({ tempData: value });
```

### Content Script設計

- 注入対象URLは必要最小限に
- DOMへの変更は最小限に
- ページのパフォーマンスを損なわない
- 名前空間の衝突を避ける

```javascript
// 良い例: 名前空間の隔離
(function() {
  const MY_EXTENSION_PREFIX = 'my-ext-';
  // DOM操作時はプレフィックスを使用
  const element = document.createElement('div');
  element.id = MY_EXTENSION_PREFIX + 'container';
})();
```

### メッセージパッシング

```javascript
// background.js → content script
chrome.tabs.sendMessage(tabId, { action: 'doSomething' });

// content script → background.js
chrome.runtime.sendMessage({ action: 'getData' }, (response) => {
  console.log(response);
});

// Popup → background.js
chrome.runtime.sendMessage({ action: 'getStatus' });
```

## Chrome Web Store公開のコツ

### 審査通過のポイント

1. **明確な目的**: 拡張機能の目的を説明文で明確に
2. **権限の正当化**: 各権限がなぜ必要か説明可能に
3. **プライバシーポリシー**: データ収集がある場合は必須
4. **高品質なアセット**: アイコン、スクリーンショットは高品質に
5. **単一目的**: 1つの拡張機能は1つの目的に集中

### よくあるリジェクト理由

| 理由 | 対策 |
|------|------|
| 過剰な権限要求 | 最小権限の原則を遵守、optional_permissions活用 |
| プライバシーポリシーの欠如 | ユーザーデータを扱う場合は必須で用意 |
| 説明と機能の不一致 | ストア説明文と実際の機能を一致させる |
| 低品質なアセット | 高解像度のアイコン、スクリーンショットを用意 |
| 単一目的違反 | 複数機能は関連性を明確に、または分割 |
| リモートコード実行 | すべてのコードを拡張機能に含める |

### ストアリスティング最適化

```
# タイトル（最大45文字）
- 機能を端的に表現
- 検索されやすいキーワードを含む

# 説明文
- 最初の132文字が検索結果に表示される
- 機能、使い方、差別化ポイントを明記
- 箇条書きで読みやすく

# スクリーンショット
- 主要機能を視覚的に説明
- 日本語UIなら日本語で
- 1280x800または640x400
```

## よくある失敗パターンと対策

### 失敗パターン1: 権限過多

**症状**: ストア審査でリジェクト、ユーザーに不信感

**対策**:
- 各権限の必要性を文書化
- optional_permissionsを活用
- activeTabで代替可能か検討

### 失敗パターン2: Service Workerの非効率

**症状**: バッテリー消費、パフォーマンス低下、予期しない停止

**対策**:
- イベントドリブン設計
- 不要なAlarmの削除
- 状態はstorageに保存
- 長時間処理は分割

### 失敗パターン3: 互換性問題

**症状**: 特定のサイトで動作しない、他の拡張と競合

**対策**:
- 主要サイトでのテスト
- Content Scriptの名前空間隔離
- エラーハンドリングの徹底
- 他の人気拡張との共存確認

### 失敗パターン4: セキュリティ脆弱性

**症状**: XSS、データ漏洩のリスク

**対策**:
- CSPの適切な設定
- ユーザー入力のサニタイズ
- evalの使用禁止
- 外部リソースの信頼性確認

## 企画フェーズ別のポイント

### Phase 1: アイデア創出

#### やるべきこと
- 自分が困っている問題から発想
- Chrome Web Storeで類似拡張を調査
- ユーザーレビューから改善点を発見

#### 避けるべきこと
- 既存拡張の完全コピー
- 需要のない機能の実装
- 技術ありきの発想

### Phase 2: 市場分析

#### やるべきこと
- WebSearchで競合を徹底調査
- ユーザー数、評価、レビューを分析
- 差別化ポイントを明確化

#### 避けるべきこと
- 競合調査を怠る
- ニッチすぎる市場を選ぶ
- 差別化なしの後発参入

### Phase 3: 設計

#### やるべきこと
- 最小権限で設計
- UIはシンプルに
- Manifest V3対応

#### 避けるべきこと
- 機能の詰め込みすぎ
- 過剰な権限要求
- 古いManifest V2での設計

### Phase 4: 公開準備

#### やるべきこと
- 高品質なアセット準備
- プライバシーポリシー作成
- 多言語対応検討

#### 避けるべきこと
- 低品質なスクリーンショット
- 曖昧な説明文
- プライバシーポリシーの欠如

## チェックリスト

### 企画完了時
- [ ] ターゲットユーザーが明確
- [ ] 競合を3つ以上分析した
- [ ] 差別化ポイントが明確
- [ ] コア機能が3〜5個に絞られている

### 開発前
- [ ] Manifest V3で設計
- [ ] 必要な権限が最小限
- [ ] Chrome APIの選定完了
- [ ] UIデザイン完了

### 公開前
- [ ] プライバシーポリシー作成済み
- [ ] 高品質なアイコン準備済み（128x128）
- [ ] スクリーンショット準備済み
- [ ] 説明文作成済み（日本語/英語）
- [ ] 主要サイトでテスト完了

### 公開後
- [ ] ユーザーフィードバックを監視
- [ ] 評価・レビューに対応
- [ ] Chrome API変更を監視
- [ ] 定期的なアップデート計画

すべてチェックできたら、Chrome Web Storeへの申請準備完了です！
