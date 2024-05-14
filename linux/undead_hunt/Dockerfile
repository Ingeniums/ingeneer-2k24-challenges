FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y socat gdb && \
    rm -rf /var/lib/apt/lists/*



RUN useradd -m ctf && \
mkdir /challenge

COPY challenge /challenge

WORKDIR /challenge



RUN chmod +x out &&\
    chmod +x run_chal.sh &&\
    chown root:root run_chal.sh &&\
    mv run_chal.sh .run_chal.sh &&\
    mkdir /tmp/cores


USER root

EXPOSE 1337

ENTRYPOINT ["./.run_chal.sh"]