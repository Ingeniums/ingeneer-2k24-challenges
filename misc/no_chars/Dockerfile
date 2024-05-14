FROM python:3-alpine

RUN apk update &&\
    apk add socat


COPY ./challenge /challenge/

WORKDIR /challenge


RUN chmod +x source.py &&\
    chmod +x run_chal.sh &&\
    chown -R root:root /challenge &&\
    mv run_chal.sh .run_chal.sh


EXPOSE 1337

ENTRYPOINT [ "./.run_chal.sh" ]