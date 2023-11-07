# 作成手順

1. Git 管理
    1. `git init`
    2. `git add .`
    3. `git commit -m "first commit"`
    4. GitHub でリモートリポジトリの作成
    5. `git remote add origin https://github.com/fuji-mizumura/templete.git`
    6. `git push -u origin main`
2. ネットワークを作成
   1. `docker network create shared-net`
3. 「server」コンテナの作成
    1. docker-compose.yml, コンテナ用ディレクトリ, Dockerfile を作成
    2. `docker compose up -d`
    3. `docker compose cp server:/usr/local/apache2/conf/httpd.conf ./server`コンテナ内のhttpd.confをホストのserverディレクトリにコピー
    4. httpd.confをマウントさせるようdocker-compose.ymlにvolumesの記述を追加
4. 「front」コンテナの作成
   1. 
