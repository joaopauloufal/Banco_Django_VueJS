FROM python:3.9.2-alpine

WORKDIR /usr/src/app/banco_django_vuejs_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev bash

RUN pip install --upgrade pip
COPY ./banco_django_vuejs_api/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

ENTRYPOINT ["./.docker/entrypoint.sh"]