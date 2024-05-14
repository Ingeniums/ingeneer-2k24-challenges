FROM ubuntu:latest


RUN apt-get update &&\
    apt-get install -y socat


COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x /challenge/out &&\
    chmod +x /challenge/run_chal.sh &&\
    chmod 777 /challenge/flag.txt &&\
    chmod +s /challenge/out


CMD ["./run_chal.sh"]