# ch06

```shell

$ git clone git@github.com:mocamocaland/microservice-apis-python.git

# orders配下に移動（kitchen側も以下のように同様の手順を実施）
$ cd ${your_path}/microservice-apis-python/ch06/orders
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
 
 
# dockerでの起動
# orders_srvice
$ docker build --no-cache -t orders_service:1.0.1 . 
$ docker run --rm -p 8000:8000 -v ${PWD}:/orders orders_service:1.0.1

# kitchen_srvice
$ docker build --no-cache -t kitchen_service:1.0.0 . 
$ docker run --rm -p 5000:5000 -v ${PWD}:/kitchen kitchen_service:1.0.0 
```