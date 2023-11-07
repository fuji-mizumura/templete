# 作成手順

1. Git 管理
    1. `git init`
    2. `git add .`
    3. `git commit -m "first commit"`
    4. GitHub でリモートリポジトリの作成
    5. `git remote add origin https://github.com/fuji-mizumura/templete.git`
    6. `git push -u origin main`
2. `docker network create shared-net`ネットワークを作成
3. 「server」コンテナの作成
    1. docker-compose.yml, コンテナ用ディレクトリ, Dockerfile を作成
    2. 
