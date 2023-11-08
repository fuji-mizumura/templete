FROM python:3.10-alpine

WORKDIR /usr/src/app
ENV FLASK_RUN_HOST=0.0.0.0

# requirements.txt をコピーして、記載されたパッケージをインストール
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-build-isolation

CMD ["flask", "run","--debugger","--reload"]

EXPOSE 5000