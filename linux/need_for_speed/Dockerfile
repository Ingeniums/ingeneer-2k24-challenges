FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

RUN useradd ctf && \
    mkdir /challenge

COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x out &&\
    chown root:root flag.txt &&\
    chmod 700 flag.txt &&\
    chmod +s out &&\
    chown ctf:ctf password.txt &&\
    chmod 777 password.txt
