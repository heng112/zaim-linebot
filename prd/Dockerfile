FROM python:3.9-slim-buster

# 必要なライブラリをインストール
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev git curl nodejs npm libsqlite3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Node.js をインストール
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g n && \
    n stable

# Jupyter Lab と必要な Python パッケージをインストール
RUN pip install --upgrade pip && \
    pip install jupyterlab ipython-sql && \
    pip install jupyterlab_sql && \
    pip install pandas && \
    pip install pyzaim && \
    pip install python-dotenv && \
    pip install line-bot-sdk && \
    pip install Flask

# ソースコードをコンテナ内にコピー
COPY . /app
WORKDIR /app


CMD ["python", "src/app.py"]
