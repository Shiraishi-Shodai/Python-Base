# //ベースにするコンテナイメージを指定
FROM ubuntu:20.04

#
USER root
# RUNコマンドはコンテナイメージ作成時に実行される
RUN apt update
RUN apt install -y python3.9
RUN apt install -y python3-pip

# COPY dockerfileにファイルを追加(リモート上の物は追加できない)、圧縮ファイルはそのままコピー
#Dockerfileが存在するディレクトリよりも親の階層を見に行くことはできないらしい。(../requirements.txtなどとするとエラーになる)
COPY requirements.txt .
RUN python3.9 -m pip install -r requirements.txt

ENV SITE_DOMAIN=vtuber.supu.com
# コンテナ内でのワークスペースを指定
WORKDIR /var

# ADD dockerfileにファイルを追加(リモート上の物も追加できる)、圧縮ファイルは解凍してコピー
ADD https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data .

# ENTRYPOINT docker runコマンド実行時に動かしたいシェルコマンドを指定
COPY script.py .
ENTRYPOINT [ "python3.9", "script.py"]