# ch14


## download
```shell
$ git clone git@github.com:mocamocaland/microservice-apis-python.git

```

## API(dockerなし)
```
# orders配下に移動（kitchen側も以下のように同様の手順を実施）
$ cd ${your_path}/microservice-apis-python/ch14/orders

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

# migrationはordersしか確認してません。
# migrationディレクトリとalembic.iniを新規で生成する場合のみ実行
(venv)$ PYTHONPATH=$(pwd) alembic revision --autogenerate -m "Initial migration"
# モデルのスキーマを作成
(venv)$ PYTHONPATH=$(pwd) alembic upgrade heads

# 仮想環境を抜ける
(venv)$ deactivate
```
 
## API(docker)
``` 
$ cd ${your_path}/microservice-apis-python/ch14
$ docker compose up

# migration実行はordersしか確認してません。
# モデルのスキーマを作成
$ docker compose exec -it api-order /bin/bash

# migrationディレクトリとalembic.iniを新規で生成する場合のみ実行
# $ PYTHONPATH=$(pwd) alembic revision --autogenerate -m "Initial migration"

# こちらは必ず実行
# $ PYTHONPATH=$(pwd) alembic upgrade heads
```

## mock API
```
# コンテナだとリクエストが送れないため以下で対応
# ここは npm install @stoplight/prism-cli でも可
$ yarn install @stoplight/prism-cli

# 各yamlファイルがあるところで実行
$ ./node_modules/.bin/prism mock kitchen.yaml --port 3000
$ ./node_modules/.bin/prism mock payments.yaml --port 3001

# curlかswaggerでレスポンスを確認
$ curl http://localhost:3000/kitchen/schedules
```


## create kubernetes cluster
```yaml
$ kubectl create deployment coffeemesh --image=api-order

# deploymentsの一覧表示
$ kubectl get deployments

$ kubectl get kubeconfig kubectl > kubeconfig

```