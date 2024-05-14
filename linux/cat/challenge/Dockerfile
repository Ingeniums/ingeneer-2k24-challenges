FROM python:3.11

RUN  apt-get update && apt-get install -y socat cron

RUN useradd  -s /bin/bash ctf

COPY entrypoint.sh /bin/entrypoint.sh

COPY flag.txt /root/flag.txt

RUN cp /bin/cat /bin/bella

RUN chmod +s /bin/bella

RUN chmod 700 /bin/entrypoint.sh 

CMD ["./bin/entrypoint.sh"]
