# ベストプラクティス

このドキュメントでは、APIサービス企画を成功させるためのベストプラクティスと実践的なガイドラインを提供します。

## 企画の原則

### API設計の原則

#### RESTful設計

```
# 良い例: リソース指向のURL
GET    /api/v1/users          # ユーザー一覧
GET    /api/v1/users/:id      # ユーザー詳細
POST   /api/v1/users          # ユーザー作成
PUT    /api/v1/users/:id      # ユーザー更新
DELETE /api/v1/users/:id      # ユーザー削除

# 避けるべき例: 動詞ベースのURL
GET    /api/v1/getUsers
POST   /api/v1/createUser
POST   /api/v1/deleteUser
```

#### HTTPメソッドの適切な使用

| メソッド | 用途 | べき等性 | セーフ |
|---------|------|---------|--------|
| GET | リソース取得 | Yes | Yes |
| POST | リソース作成 | No | No |
| PUT | リソース全体更新 | Yes | No |
| PATCH | リソース部分更新 | No | No |
| DELETE | リソース削除 | Yes | No |

#### ステータスコードの適切な使用

```
# 成功系
200 OK           - GET/PUT/PATCHの成功
201 Created      - POSTでリソース作成成功
204 No Content   - DELETEの成功

# クライアントエラー
400 Bad Request  - 入力値エラー
401 Unauthorized - 認証エラー
403 Forbidden    - 権限エラー
404 Not Found    - リソース不存在
409 Conflict     - 競合（重複など）
422 Unprocessable Entity - バリデーションエラー
429 Too Many Requests - レート制限

# サーバーエラー
500 Internal Server Error - サーバー内部エラー
503 Service Unavailable  - メンテナンス等
```

#### バージョニング

```
# URLパスでのバージョニング（推奨）
GET /api/v1/users
GET /api/v2/users

# 後方互換性の維持
- 既存フィールドの削除は非推奨化してから
- 新フィールドの追加は後方互換
- 破壊的変更はメジャーバージョンアップ
```

### セキュリティ最優先

#### 認証・認可

```python
# API Key認証（シンプル）
headers = {
    "X-API-Key": "your-api-key"
}

# JWT認証（推奨）
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIs..."
}

# OAuth2.0（サードパーティ連携）
# - Authorization Code Grant（Webアプリ）
# - Client Credentials Grant（サーバー間通信）
```

#### 入力検証

```python
# すべての入力を検証
def create_user(request):
    # 型チェック
    if not isinstance(request.email, str):
        raise ValidationError("email must be string")

    # フォーマットチェック
    if not is_valid_email(request.email):
        raise ValidationError("Invalid email format")

    # 長さチェック
    if len(request.name) > 100:
        raise ValidationError("name too long")

    # SQLインジェクション対策
    # パラメータバインディングを使用
    db.execute("SELECT * FROM users WHERE email = ?", [request.email])
```

#### レート制限

```python
# レート制限の実装
# - 固定ウィンドウ: シンプル、バースト問題あり
# - スライディングウィンドウ: バースト対策、複雑
# - トークンバケット: 柔軟、複雑

# レスポンスヘッダー例
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1234567890
Retry-After: 60  # 429時のみ
```

### スケーラビリティ設計

#### 水平スケーリング

```yaml
# ステートレス設計
- セッションは外部ストア（Redis）に保存
- 各インスタンスは同等の処理が可能
- ロードバランサーで分散

# データベース接続プール
- コネクションプールを使用
- 接続数の上限を設定
- コネクションリークを防ぐ
```

#### キャッシュ戦略

```python
# キャッシュレイヤー
# 1. CDN（静的コンテンツ）
# 2. API Gateway（レスポンスキャッシュ）
# 3. アプリケーション（Redis）
# 4. データベース（クエリキャッシュ）

# キャッシュパターン
# Cache-Aside: アプリが明示的にキャッシュ操作
def get_user(user_id):
    # キャッシュ確認
    cached = redis.get(f"user:{user_id}")
    if cached:
        return cached

    # DBから取得
    user = db.get_user(user_id)

    # キャッシュに保存
    redis.setex(f"user:{user_id}", 3600, user)
    return user
```

### ドキュメント重視

#### OpenAPI/Swagger

```yaml
# openapi.yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users:
    get:
      summary: ユーザー一覧取得
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
```

#### 開発者体験

```
# 良いドキュメントの要素
- 認証方法の説明
- エンドポイント一覧
- リクエスト/レスポンス例
- エラーコード一覧
- SDKサンプルコード
- 変更履歴
```

## よくある失敗パターンと対策

### 失敗パターン1: 一貫性のないAPI設計

**症状**: エンドポイントごとに異なる命名規則、レスポンス形式

**対策**:
- API設計ガイドラインの策定
- レビュープロセスの導入
- OpenAPI仕様での一元管理

### 失敗パターン2: セキュリティの軽視

**症状**: 認証なしのエンドポイント、入力検証不足

**対策**:
- セキュリティレビューの必須化
- ペネトレーションテスト
- OWASP Top 10への対応

### 失敗パターン3: スケーラビリティの欠如

**症状**: 負荷増加時のパフォーマンス低下

**対策**:
- 負荷テストの実施
- キャッシュ戦略の導入
- オートスケーリング設定

### 失敗パターン4: 不十分なエラーハンドリング

**症状**: 500エラーの多発、デバッグ困難

**対策**:
- 統一されたエラーレスポンス形式
- 適切なエラーコード体系
- 詳細なログ出力

## 企画フェーズ別のポイント

### Phase 1: 設計

#### やるべきこと
- API仕様ファーストアプローチ
- OpenAPI仕様書の作成
- セキュリティ設計の明確化

#### 避けるべきこと
- 実装しながら設計
- セキュリティ後回し
- ドキュメントなしでの開発

### Phase 2: 開発

#### やるべきこと
- テスト駆動開発
- CI/CDパイプライン構築
- コードレビューの実施

#### 避けるべきこと
- テストなしでの実装
- 手動デプロイ
- 単独での開発

### Phase 3: 運用

#### やるべきこと
- 監視・アラートの設定
- インシデント対応計画
- 定期的なセキュリティ更新

#### 避けるべきこと
- 監視なしでの運用
- インシデント対応の未整備
- 依存関係の放置

## チェックリスト

### 企画完了時
- [ ] API利用者が明確
- [ ] エンドポイント設計完了
- [ ] セキュリティ設計完了
- [ ] インフラ設計完了
- [ ] SLA目標設定完了

### 開発前
- [ ] OpenAPI仕様書作成
- [ ] 認証方式決定
- [ ] データベース設計完了
- [ ] エラーハンドリング設計完了
- [ ] テスト戦略策定

### 本番前
- [ ] セキュリティレビュー完了
- [ ] 負荷テスト完了
- [ ] 監視・アラート設定完了
- [ ] ドキュメント整備完了
- [ ] インシデント対応計画策定

### 本番後
- [ ] メトリクス監視中
- [ ] エラーレート監視中
- [ ] 定期的なセキュリティ更新
- [ ] ユーザーフィードバック収集

すべてチェックできたら、本番リリース準備完了です！
