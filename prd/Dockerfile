FROM python:3.9-slim-buster

# 必要なライブラリをインストール
RUN apt-get update && \
    apt-get install -y git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 必要な Python パッケージをインストール
RUN pip install --upgrade pip && \
    pip install pandas && \
    pip install pyzaim && \
    pip install python-dotenv && \
    pip install line-bot-sdk && \
    pip install Flask

# ソースコードをコンテナ内にコピー
COPY . /app
WORKDIR /app


CMD ["python", "line.py"]
