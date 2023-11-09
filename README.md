# コンテナ構成

-   **server:** Appache 公式イメージ(https://hub.docker.com/_/httpd)
    -   理由：実装例が豊富で特に php とセットにすることが多いため
-   **front:** Node.js 公式イメージに Next.js をインストール(https://hub.docker.com/_/node)
    -   理由：純粋な react を触ったことがないので
-   **api:** python 公式イメージに Flask をインストール(https://hub.docker.com/_/python)、
    -   理由：php だとテスト用環境構築の際に Apache の設定が専用設定になってしまうため
-   **db:** postgresql 公式イメージ(https://hub.docker.com/_/postgres)
    -   理由：公式コンテナのなかで唯一 Alpine をリリースしていて、イメージサイズが半分ほどで済むため

# 作成手順

1.  **Git 管理**
    1. `git init`
    2. `git add .`
    3. `git commit -m "first commit"`
    4. GitHub でリモートリポジトリの作成
    5. `git remote add origin https://github.com/fuji-mizumura/templete.git`
    6. `git push -u origin main`
2.  **ネットワークを作成**
    1. `docker network create shared-net`
3.  **「server」コンテナの作成**
    1. docker-compose.yml, コンテナ用ディレクトリ, Dockerfile を作成
    2. `docker compose up -d`
    3. `docker compose cp server:/usr/local/apache2/conf/httpd.conf ./server`コンテナ内の httpd.conf をホストの server ディレクトリにコピー
    4. httpd.conf をマウントさせるよう docker-compose.yml に volumes の記述を追加
    5. localhost（ポート指定なし）で動作を確認
4.  **「front」コンテナの作成**
    1. docker-compose.yml に追記, コンテナ用ディレクトリ, Dockerfile を作成
    2. `docker compose up -d`
    3. `docker compose exec front ash`
    4. `npm install next@latest react@latest react-dom@latest`
    5. .gitignore を作成、package.json に scripts を追記、app/page.tsx、app/layout.tsx を作成
    6. `npm run dev`で起動し、localhost:3000 でのレスポンスを確認
    7. Dockerfile に`CMD [ "npm","run","dev" ]`を追記
5.  **「api」コンテナの作成**
    1. docker-compose.yml に追記, コンテナ用ディレクトリ, Dockerfile を作成
    2. ※今回は前回のテストで使用した Flask の api ディレクトリを丸ごとコピーした
    3. localhost:5000 でのレスポンスを確認
6.  **「db」コンテナの作成**
    1. docker-compose.yml に追記, コンテナ用ディレクトリ, Dockerfile を作成
    2. .gitignore の作成
7. **httpd.confを修正**
   1. 142行目mod_proxy.soをアクティブ化
   2. 145行目mod_proxy_http.soをアクティブ化
   3. 241行目ServerNameの変更（今回はlocalhostにした）
   4. 265~292行目DocumentRoot関連の全ての内容をコメントアウト
   5. 552行目以降にリバースプロキシの設定を記述
   6. コンテナを再起動か`httpd -k restart`で設定を反映させ、localhostとlocalhost/apiにアクセスしてレスポンスを確認
8. 「api」から「db」への疎通確認
   1. データベースの環境変数を「api」内のコードとして反映、またそれに伴ってコードを修正
   2. 「api」から「db」へアクセスしてデータ取得を確認

# 目標

-   1 プロセス、1 コンテナ、1 インスタンスで AWS サーバーを建てきる
-   SSL 証明を取得、設定する
-   EC2 インスタンスをコピーしてみる
-   踏み台サーバー？
