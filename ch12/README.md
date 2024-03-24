# ch12

```shell

$ git clone git@github.com:mocamocaland/microservice-apis-python.git

# orders配下に移動（kitchen側も以下のように同様の手順を実施）
$ cd ${your_path}/microservice-apis-python/ch12/orders
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
(venv)$ uvicorn app:app --reload
# kitchen_service
(venv)$ flask run --reload

# 仮想環境を抜ける
(venv)$ deactivate
``` 
 
## API(docker)
``` 
$ cd ${your_path}/microservice-apis-python/ch12
$ docker compose up
```

## テスト実行
```
# node, dreddをインストール
$ node -v
v20.11.1
$ npm install dredd
# テストを実行
$ ./node_modules/.bin/dredd orders/oas.yaml http://localhost:8000 --server "docker-compose run --rm api-order uvicorn app:app --reload"

```