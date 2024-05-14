FROM python:3-alpine

RUN apk update && \
    apk add socat

COPY ./challenge /challenge

WORKDIR /challenge

RUN chmod +x entrypoint.sh wordle.py 

EXPOSE 1224

ENTRYPOINT ["./entrypoint.sh"]