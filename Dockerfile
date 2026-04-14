# 軽量版Pythonを使用
FROM python:3.10-slim

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のコピーとインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY . .

# Cloud Runのポート(通常8080)で起動
# uvicornを使ってFastAPIを立ち上げる
CMD ["uvicorn", "main:api_app", "--host", "0.0.0.0", "--port", "8080"]
