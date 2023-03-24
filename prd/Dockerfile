FROM python:3.9-slim-buster

# 必要なライブラリをインストール
RUN apt-get update && \
    apt-get install -y git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/ 

# 必要な Python パッケージをインストール
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# ソースコードをコンテナ内にコピー
COPY . /app
WORKDIR ./app/app

CMD ["python", "line.py"]
