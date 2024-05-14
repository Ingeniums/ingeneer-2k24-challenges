FROM python:3.11

RUN apt-get update && \
    apt-get install -y socat 

COPY challenge/files /app/


RUN chmod 700 /app/entrypoint.sh 

CMD [ "/app/entrypoint.sh" ]    
