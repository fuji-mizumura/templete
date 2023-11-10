FROM node:21-alpine3.17

WORKDIR /usr/src/app

# package-lock.jsonのみでモジュールをインストールするnpm ciを利用する
COPY app/package*.json ./
RUN npm ci

CMD [ "npm","run","dev" ]

EXPOSE 3000