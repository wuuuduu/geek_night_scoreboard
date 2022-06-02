FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /code/backend/

RUN apt-get update && apt-get -y install build-essential git libmagic-dev libpcre3 libpcre3-dev && apt-get upgrade -y

RUN pip install uwsgi

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
