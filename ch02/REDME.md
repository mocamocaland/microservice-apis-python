# microservice_apis_master_ch2

```shell
# venv作成
$ cd ${your_path}/microservice_apis_master_ch2
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
```