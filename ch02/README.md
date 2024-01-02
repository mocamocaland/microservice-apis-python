# ch02

```shell

$ git clone git@github.com:mocamocaland/microservice-apis-python.git
# venv作成
$ cd ${your_path}/microservice-apis-python/ch02
$ python3 -m venv venv
# 仮想環境に入る
$ souce venv/bin/activate
# ライブラリインストール
(venv)$ pip install -r requirements.txt
# アプリケーション実行、API挙動の確認
(venv)$ uvicorn orders.app:app --reload

# 仮想環境を抜ける
(venv)$ deactivate
# 再度入る場合
$ souce venv/bin/activate
 
 
# dockerfileから実行
$ docker build --no-cache -t orders_service:1.0.0 . 
$ docker run --rm -p 8000:8000 orders_service:1.0.0 uvicorn orders.app:app --host 0.0.0.0 --port 8000 --reload

```