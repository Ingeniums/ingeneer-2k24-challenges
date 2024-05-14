FROM ubuntu:latest


RUN apt-get update && apt-get install -y \
    python3 \
    socat &&\
    rm -rf /var/lib/apt/lists/* 


COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x source.py && \
    chmod +x run_chal.sh


ENTRYPOINT [ "./run_chal.sh" ]