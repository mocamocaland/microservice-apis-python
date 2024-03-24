# ch12

## Docker
```shell
$ git clone git@github.com:mocamocaland/microservice-apis-python.git
$ cd ${your_path}/microservice-apis-python/ch12
$ docker compose up
```

## テスト実行
```
# node, dreddをインストール
$ node -v
v20.11.1
$ npm install dredd

# テスト実行
# dredd
$ ./node_modules/.bin/dredd orders/oas.yaml http://localhost:8000 --server "docker-compose run --rm api-order uvicorn app:app --reload"
$ ./node_modules/.bin/dredd orders/oas.yaml http://localhost:8000 --server "docker-compose run --rm api-order uvicorn app:app --reload" --hookfiles=./orders/hooks.py --language=python
$ ./node_modules/.bin/dredd orders/oas.yaml http://localhost:8000 --server "docker-compose run --rm api-order uvicorn app:app --reload" --hooks-worker-handler=./orders/hooks.py --language=python

# schemathesis
$ docker compose exec -it api-order-test /bin/bash
# コンテナ内で実行する
root@d254bdc8deb0:/orders# schemathesis run oas.yaml --base-url=http://localhost:8001  --hypothesis-database=none

```
