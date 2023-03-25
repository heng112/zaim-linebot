## zaimの購入履歴データを活用した LINE BOT

### 概要

LINE BOT で手軽に商品の相場を確認したい！

### 機能要件

入力値 に対して適切な出力を返すこと

- 入力値 -> 商品名
- 出力値 -> 購入できる店舗と金額の提示

### 開発手順

- [x] zaimAPIから購入履歴データを収集
- [x] 取集データをDBに格納
- [x] LINE BOTを構築 
- [x] LINE BOT と DBを接続する
- [ ] 適切に出力するアルゴリズムを構築する
- [ ] zaim APIから DBに定期的に取り込むデータパイプラインを構築


### 環境構築(dev , test)

- Dockerイメージをビルドする

```
docker build -t zaim-bot .
docker build -t test-lszaim-bot .
```

- Dockerコンテナを起動する

```
docker run -it --rm -p 8888:8888 -v $PWD:/app zaim-bot
docker run --rm -p 5001:80 -v ${PWD}/app:/app test-zaim-bot
```

- jupyter lab にアクセス

```
http://localhost:8888/lab
```

-  SQLlite

SQLiteをロードする。
```perl
%load_ext sql
```
SQLiteのDBファイルを作成する。
```perl
%sql sqlite:///my_zaim.db
```


#### 使用技術
- python
- Docker
- SQLlite
- render



## 後でやりたいこと

- duckDBに移管
- dbtを組み込む
- CI/CDを構築