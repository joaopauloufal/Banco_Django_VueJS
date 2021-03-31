FROM node:14.16.0-alpine3.10

RUN apk add --no-cache nano bash g++ gcc libgcc libstdc++ linux-headers make yarn

WORKDIR /usr/src/app/banco_django_vuejs_frontend

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

COPY . .

EXPOSE 3000

ENTRYPOINT ["./.docker/entrypoint.sh"]