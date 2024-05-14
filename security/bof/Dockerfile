FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat

COPY ./challenge /challenge

WORKDIR /challenge

RUN chmod +x out &&\
    chmod +x run_chal.sh


EXPOSE 1337

ENTRYPOINT [ "./run_chal.sh" ]