FROM python:3.7.9-buster

RUN pip install --upgrade pip

WORKDIR /dat

COPY requirements.txt ./

RUN apt-get update && \
    apt-get install -y vim && \
    apt-get install -y nano && \
    pip3 install -r requirements.txt --upgrade
