FROM python:3.11

RUN  apt-get update && apt-get install -y socat

COPY ./entrypoint.sh /bin/entrypoint.sh

COPY main.py /app/main.py

RUN chmod 700 /bin/entrypoint.sh 

CMD ["/bin/entrypoint.sh"]