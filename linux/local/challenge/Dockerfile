FROM python:3.11

RUN  apt-get update && apt-get install -y socat netcat-traditional cron

RUN useradd -s /bin/bash ctf

COPY ./entrypoint.sh /bin/entrypoint.sh

COPY server.py /root/server.py

RUN chmod 700 /bin/entrypoint.sh 

EXPOSE 12345

CMD ["/bin/entrypoint.sh"]
