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
    pip install Flask && \
    jupyter serverextension enable --py jupyterlab_sql --sys-prefix && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib && \
    jupyter labextension install @jupyterlab/translation-extension
    # pip install jupyterlab-language-pack-ja


# ソースコードをコンテナ内にコピー
COPY . /src
WORKDIR /src

# ポート番号8888を開放
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
