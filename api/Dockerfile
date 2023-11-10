FROM python:3.10-alpine

# 作業ディレクトリを指定
WORKDIR /usr/src/app

# 環境変数を指定
ENV FLASK_RUN_HOST=0.0.0.0

# requirements.txt をコピーして、記載されているパッケージをインストール
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-build-isolation

CMD ["flask", "run","--debugger","--reload"]

EXPOSE 5000