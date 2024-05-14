FROM python:3-alpine

RUN apk update &&\
    apk add socat


COPY ./challenge /challenge/

WORKDIR /challenge


RUN chmod +x source.py &&\
    chmod +x run_chal.sh &&\
    chown -R root:root /challenge

EXPOSE 1337

ENTRYPOINT [ "./run_chal.sh" ]