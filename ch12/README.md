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
# hooksなし
$ ./node_modules/.bin/dredd orders/oas.yaml http://localhost:8000 --server "docker-compose run --rm api-order uvicorn app:app --reload"
# hooksあり
$ ./node_modules/.bin/dredd orders/oas.yaml http://localhost:8000 --server "docker-compose run --rm api-order uvicorn app:app --reload" --hooks-worker-handler=./orders/hooks.py --language=python

# schemathesis
# コンテナ内で実行
$ docker compose exec -it api-order-test /bin/bash
# Schemathesisを実行
root@d254bdc8deb0:/orders# schemathesis run oas.yaml --base-url=http://localhost:8001  --hypothesis-database=none
# Schemathesisテストスイートの出力
root@d254bdc8deb0:/orders# schemathesis run oas_with_links.yaml --base-url=http://localhost:8001 --stateful=links
# 全てのチェックの適用
root@d254bdc8deb0:/orders# schemathesis run oas_with_links.yaml --base-url=http://localhost:8001 --hypothesis-database=none --stateful=links --checks=all

# GraphQL
$  docker compose exec -it api-product-test /bin/bash
# Schemathesisを実行
root@c79f41361c9b:/products# schemathesis run --hypothesis-deadline=None http://localhost:8003/graphql

```

