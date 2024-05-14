FROM python:3-alpine

RUN apk update && \
    apk add socat && pip install pycryptodome

COPY ./challenge /challenge

WORKDIR /challenge

RUN chmod +x entrypoint.sh server.py 

EXPOSE 1337

ENTRYPOINT ["./entrypoint.sh"]