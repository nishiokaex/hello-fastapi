# Hello FastAPI

FastAPIを使用したシンプルなWebAPIプロジェクトです。Vercelでのデプロイに対応しています。

## 🚀 デプロイ状況

**プレビュー環境**: https://hello-fastapi-ox4g674p3-nishiokaexs-projects.vercel.app

## 📋 API エンドポイント

| エンドポイント | メソッド | 説明 | レスポンス例 |
|---|---|---|---|
| `/` | GET | ルートエンドポイント | `{"message": "Hello World from Vercel!"}` |
| `/health` | GET | ヘルスチェック | `{"status": "healthy"}` |
| `/api/hello` | GET | 基本的なAPIエンドポイント | `{"message": "Hello from FastAPI API!"}` |
| `/api/hello/{name}` | GET | パラメータ付きエンドポイント | `{"message": "Hello {name}!"}` |

## 🛠️ 技術スタック

- **フレームワーク**: FastAPI
- **ランタイム**: Python 3.9+
- **デプロイ**: Vercel
- **依存関係管理**: pip + requirements.txt

## 📁 プロジェクト構成

```
hello-fastapi/
├── index.py          # Vercel用メインアプリケーション
├── main.py           # ローカル開発用アプリケーション  
├── api/index.py      # API関数
├── requirements.txt  # Python依存関係
├── vercel.json       # Vercel設定
├── CLAUDE.md         # 開発ガイドライン
└── README.md         # このファイル
```

## 🚀 ローカル開発

### セットアップ

```bash
# 仮想環境の作成
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate     # Windows

# 依存関係のインストール
pip install -r requirements.txt
```

### 開発サーバーの起動

```bash
uvicorn main:app --reload
```

http://localhost:8000 でアプリケーションにアクセスできます。

### API ドキュメント

FastAPIの自動生成ドキュメントが利用できます：
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🌐 Vercelデプロイ

### プレビューデプロイ

```bash
vercel
```

### プロダクションデプロイ

```bash
vercel --prod
```

## 📝 開発フロー

1. `feature/[機能名]` ブランチを作成
2. 機能開発
3. Vercelプレビュー環境でテスト
4. コミット・プッシュ
5. Pull Request作成・マージ

詳細は [CLAUDE.md](./CLAUDE.md) を参照してください。

## 🤝 貢献

プルリクエストやイシューの報告を歓迎します。

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。
