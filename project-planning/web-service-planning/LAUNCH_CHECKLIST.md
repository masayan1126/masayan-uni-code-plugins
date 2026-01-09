# 新規サイト立ち上げチェックリスト

このチェックリストは、新しいWebサイトを公開する際に必要な設定項目を優先度順にまとめたものです。

## 🔴 最優先（サイト公開前に必須）

### 1. 独自ドメインの設定

- [ ] ドメイン名の選定と登録
- [ ] DNSレコードの設定
  - [ ] Aレコード/AAAAレコード（IPv4/IPv6）
  - [ ] CNAMEレコード（サブドメイン用）
  - [ ] MXレコード（メール用、必要に応じて）
  - [ ] TXTレコード（各種認証用）
- [ ] ネームサーバー設定（レジストラ側）
- [ ] www有無の統一設定（リダイレクト）

### 2. SSL証明書の導入

- [ ] 証明書の取得
  - [ ] Let's Encrypt（無料、自動更新）
  - [ ] 有料証明書（EV/ワイルドカードなど、必要に応じて）
- [ ] 自動更新の設定（Let's Encryptの場合）
- [ ] HTTPSリダイレクトの設定（HTTP → HTTPS強制）
- [ ] HSTS設定（Strict-Transport-Securityヘッダー）
- [ ] Mixed Contentの解消（すべてのリソースをHTTPS化）

### 3. 基本的なメタデータの設定

- [ ] 各ページの`<title>`タグ（30-60文字）
- [ ] `<meta name="description">`タグ（120-160文字）
- [ ] `<meta name="keywords">`タグ（オプション）
- [ ] ファビコンの設定
- [ ] OGPタグの設定（Facebook/Twitter共有用）
  - [ ] `og:title`
  - [ ] `og:description`
  - [ ] `og:image`
  - [ ] `og:url`
  - [ ] `og:type`
- [ ] Twitterカード設定（`twitter:card`など）

---

## 🟡 高優先（公開後早期に設定）

### 4. XMLサイトマップの生成

- [ ] `sitemap.xml`の作成
- [ ] 動的生成の仕組み（CMS連動、必要に応じて）
- [ ] **静的サイトジェネレーション（SSG）の場合**
  - [ ] CMSからの記事データを事前取得（ビルド時）
  - [ ] 全ページを静的HTMLとして事前生成
  - [ ] サイトマップもビルド時に自動生成
  - [ ] ビルドトリガーの設定（CMS更新時の自動ビルド）
- [ ] `robots.txt`にサイトマップの場所を記載
- [ ] 画像サイトマップ（必要に応じて）
- [ ] サイトマップの圧縮（.xml.gz、必要に応じて）

### 5. Google Search Consoleの設定

- [ ] プロパティの追加（ドメインプロパティ推奨）
- [ ] 所有権の確認
  - [ ] DNSレコード（推奨）
  - [ ] HTMLファイルアップロード
  - [ ] メタタグ
  - [ ] Google Analytics連携
- [ ] サイトマップの送信（`/sitemap.xml`）
- [ ] 重要ページのインデックスリクエスト
- [ ] Coreウェブバイタルの確認

### 6. アナリティクス・トラッキング設定

- [ ] Google Analytics 4の設定
  - [ ] プロパティ作成
  - [ ] トラッキングコード設置
  - [ ] コンバージョン設定
  - [ ] イベント設定
- [ ] Google Tag Managerの導入（推奨）
- [ ] プライバシーポリシーページの作成
- [ ] Cookie同意バナーの設置（GDPR/CCPA対応、必要に応じて）

---

## 🟢 中優先（公開後1-2週間以内）

### 7. パフォーマンス最適化

- [ ] CDNの設定（CloudflareやCloudFrontなど）
- [ ] ブラウザキャッシュの設定
  - [ ] Cache-Controlヘッダー
  - [ ] ETagヘッダー
- [ ] サーバーキャッシュの設定
- [ ] 画像最適化
  - [ ] 圧縮（TinyPNG、ImageOptimなど）
  - [ ] WebP対応
  - [ ] レスポンシブ画像（srcset）
  - [ ] 遅延読み込み（lazy loading）
- [ ] CSS/JSの最小化・結合
- [ ] Gzip/Brotli圧縮の有効化
- [ ] Core Web Vitalsの測定と改善
  - [ ] LCP（Largest Contentful Paint）
  - [ ] FID（First Input Delay）
  - [ ] CLS（Cumulative Layout Shift）

### 8. セキュリティ強化

- [ ] WAF（Web Application Firewall）の設定
- [ ] セキュリティヘッダーの設定
  - [ ] Content-Security-Policy（CSP）
  - [ ] X-Frame-Options
  - [ ] X-Content-Type-Options
  - [ ] Referrer-Policy
  - [ ] Permissions-Policy
- [ ] バックアップ設定
  - [ ] 定期的な自動バックアップ（日次推奨）
  - [ ] バックアップの復元テスト
  - [ ] オフサイトバックアップ
- [ ] SQLインジェクション対策
- [ ] XSS対策
- [ ] CSRF対策

### 9. サーバー監視・通知

- [ ] アップタイム監視（UptimeRobotなど）
- [ ] エラー通知の設定
- [ ] サーバーリソース監視（CPU、メモリ、ディスク）
- [ ] エラーログ監視
- [ ] パフォーマンス監視（APMツール、必要に応じて）

---

## 🔵 低優先（公開後1ヶ月以内）

### 10. 高度なSEO対策

- [ ] 構造化データの実装（JSON-LD形式）
  - [ ] Organization
  - [ ] WebSite
  - [ ] BreadcrumbList
  - [ ] Article（ブログの場合）
  - [ ] Product（ECサイトの場合）
- [ ] カノニカルタグの設定
- [ ] hreflangタグ（多言語サイトの場合）
- [ ] パンくずリストの実装
- [ ] 404ページのカスタマイズ
- [ ] リダイレクト設定（301/302）
- [ ] Google My Businessの登録（ローカルビジネスの場合）

### 11. CMS固有の設定（該当する場合）

- [ ] 管理画面のSSL化
- [ ] 二要素認証の有効化
- [ ] 管理者アカウントの権限管理
- [ ] ユーザーロールの設定
- [ ] 不要なプラグイン・テーマの削除
- [ ] データベースの最適化
- [ ] セキュリティプラグインの導入

### 12. 追加の分析・マーケティングツール

- [ ] Microsoft Clarity（ヒートマップ、セッション記録）
- [ ] Hotjar（ユーザー行動分析）
- [ ] Google Search Ads（必要に応じて）
- [ ] Facebook Pixel（広告運用の場合）
- [ ] LinkedIn Insight Tag（B2Bの場合）

---

## 📋 実装の優先順位まとめ

### フェーズ1：公開前（必須）
1. ドメイン設定
2. SSL証明書
3. 基本的なメタデータ

### フェーズ2：公開直後（1週間以内）
4. サイトマップ
5. Search Console
6. Analytics

### フェーズ3：公開後早期（1-2週間）
7. パフォーマンス最適化
8. セキュリティ強化
9. 監視設定

### フェーズ4：公開後改善（1ヶ月以内）
10. 高度なSEO対策
11. CMS固有設定
12. 追加の分析ツール

---

## 💡 補足事項

### ドメイン設定の注意点
- DNS設定の反映には最大48時間かかる場合があるため、余裕を持って設定する
- メールサーバーを使用する場合は、SPF/DKIM/DMARCレコードも設定する

### SSL証明書の選択基準
- 個人サイト・スタートアップ → Let's Encrypt（無料）
- 企業サイト → 有料証明書（組織認証）
- ECサイト・金融 → EV証明書（拡張認証）

### パフォーマンス目標値
- PageSpeed Insights：90点以上（モバイル/デスクトップ）
- LCP：2.5秒以内
- FID：100ミリ秒以内
- CLS：0.1以内

### セキュリティチェック
- [Mozilla Observatory](https://observatory.mozilla.org/)でセキュリティヘッダーをチェック
- [SSL Labs](https://www.ssllabs.com/ssltest/)でSSL設定をチェック
