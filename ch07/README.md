# ch07

```shell
# download
$ git clone git@github.com:mocamocaland/microservice-apis-python.git

# orders配下に移動（kitchen側も以下のように同様の手順を実施）
$ cd ${your_path}/microservice-apis-python/ch07/orders
# venvを作成(mac)
$ python3 -m venv venv
# venvを作成(win)
$ python -m venv .venv

# 仮想環境に入る(mac)
$ souce venv/bin/activate
# 仮想環境に入る(win)
$ .venv\Scripts\activate.bat

# ライブラリインストール
(venv)$ pip install -r requirements.txt

# アプリケーション起動
# orders_service
(venv)$ uvicorn orders.web.app:app --reload
# kitchen_service
(venv)$ flask run --reload

# migrationディレクトリとalembic.iniを新規で生成する場合のみ実行
(venv)$ PYTHONPATH=$(pwd) alembic revision --autogenerate -m "Initial migration"
# モデルのスキーマを作成
(venv)$ PYTHONPATH=$(pwd) alembic upgrade heads

# 仮想環境を抜ける
(venv)$ deactivate
```
 
## API(docker)
``` 
$ cd ${your_path}/microservice-apis-python/ch07/
$ docker compose up

# migration実行,モデルのスキーマを作成
$ docker compose exec -it api-order /bin/bash

# migrationディレクトリとalembic.iniを新規で生成する場合のみ実行
# $ PYTHONPATH=$(pwd) alembic revision --autogenerate -m "Initial migration"
# $ PYTHONPATH=$(pwd) alembic upgrade heads


# 個別でビルド、ランをする場合
# orders_service
$ docker build --no-cache -t orders_service:1.0.2 . 
$ docker run --rm -p 8000:8000 -v ${PWD}:/orders orders_service:1.0.2

# kitchen_srvice
$ docker build --no-cache -t kitchen_service:1.0.0 . 
$ docker run --rm -p 5000:5000 -v ${PWD}:/kitchen kitchen_service:1.0.0 
```

## mock API
```
# コンテナだとリクエストが遅れないため以下で対応
# ここは npm install @stoplight/prism-cli でも可
$ yarn install @stoplight/prism-cli

# 各yamlファイルがあるところで実行
$ ./node_modules/.bin/prism mock kitchen.yaml --port 3000
$ ./node_modules/.bin/prism mock payments.yaml --port 3001

# curlかswaggerでレスポンスを確認
$ curl http://localhost:3000/kitchen/schedules
```