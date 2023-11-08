# 作成手順

1.  Git 管理
    1. `git init`
    2. `git add .`
    3. `git commit -m "first commit"`
    4. GitHub でリモートリポジトリの作成
    5. `git remote add origin https://github.com/fuji-mizumura/templete.git`
    6. `git push -u origin main`
2.  ネットワークを作成
    1. `docker network create shared-net`
3.  「server」コンテナの作成
    1. docker-compose.yml, コンテナ用ディレクトリ, Dockerfile を作成
    2. `docker compose up -d`
    3. `docker compose cp server:/usr/local/apache2/conf/httpd.conf ./server`コンテナ内の httpd.conf をホストの server ディレクトリにコピー
    4. httpd.conf をマウントさせるよう docker-compose.yml に volumes の記述を追加
4.  「front」コンテナの作成
    1. docker-compose.yml に追記, コンテナ用ディレクトリ, Dockerfile を作成
    2. `docker compose up -d`
    3. `docker compose exec front ash`
    4. `npm install next@latest react@latest react-dom@latest`
    5. .gitignore を作成、package.json に scripts を追記、app/page.tsx、app/layout.tsx を作成
    6. 

# 目標

-   1 プロセス、1 コンテナ、1 インスタンスで AWS サーバーを建てきる
-   SSL 証明を取得、設定する
-   EC2 インスタンスをコピーしてみる
-   踏み台サーバー？
