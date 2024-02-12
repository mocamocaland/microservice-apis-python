# ch07

## 共通

```shell
# download
$ git clone git@github.com:mocamocaland/microservice-apis-python.git

# orders配下に移動（kitchen側も以下のように同様の手順を実施）
$ cd ${your_path}/microservice-apis-python/ch07/orders
```
## orders, kitchen  mac
```
# venvを作成(mac)
$ python3 -m venv venv

# 仮想環境に入る(mac)
$ souce venv/bin/activate

# アプリケーション起動
# orders_service
(venv)$ uvicorn orders.web.app:app --reload
# kitchen_service
(venv)$ flask run --reload

# migrationディレクトリとalembic.iniを新規で生成する場合
(venv)$ PYTHONPATH=$(pwd) alembic revision --autogenerate -m "Initial migration"
# モデルのスキーマを作成
(venv)$ PYTHONPATH=$(pwd) alembic upgrade heads

# 仮想環境を抜ける
(venv)$ deactivate
# 再度入る場合
$ souce venv/bin/activate
```

## orders, kitchen  win
```
# venvを作成(win)
$ python -m venv .venv
# 仮想環境に入る(win)
$ .venv\Scripts\activate.bat

# ライブラリインストール
(venv)$ pip install -r requirements.txt

# アプリケーション起動
# orders_service
(venv)$ uvicorn orders.web.app:app --reload
# kitchen_service
(venv)$ flask run --reload

# 初回の構築時のみ実行
# migrationディレクトリとalembic.iniを新規で生成する場合のみ実行
(venv)$ PYTHONPATH=$(pwd) alembic revision --autogenerate -m "Initial migration"
# モデルのスキーマを作成
(venv)$ PYTHONPATH=$(pwd) alembic upgrade heads

# 仮想環境を抜ける
(venv)$ deactivate
# 再度入る場合
$ .venv\Scripts\activate.bat
 
 ```


## Docker
```
# dockerでの起動
$ docker compose up

# 初回の構築時のみ実行
# スキーマ作成のため、コンテナ内にアクセス
$ docker compose exec -it api-order /bin/bash
# migrationディレクトリとalembic.iniを新規で生成する場合のみ実行
# PYTHONPATH=$(pwd) alembic revision --autogenerate -m "Initial migration"
# モデルのスキーマを作成
# PYTHONPATH=$(pwd) alembic upgrade heads


# 個別でbuild、runをする場合
# orders_service
$ docker build --no-cache -t orders_service:1.0.2 . 
$ docker run --rm -p 8000:8000 -v ${PWD}:/orders orders_service:1.0.2

# kitchen_srvice
$ docker build --no-cache -t kitchen_service:1.0.0 . 
$ docker run --rm -p 5000:5000 -v ${PWD}:/kitchen kitchen_service:1.0.0 
```