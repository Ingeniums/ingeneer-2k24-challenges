FROM python:3.11

RUN apt update && apt install -y socat

COPY ./entrypoint.sh /bin/entrypoint.sh

COPY flag0.txt /tmp/amira/flag0.txt

COPY main.py /app/main.py

RUN chmod 444 /tmp/amira/flag0.txt

RUN chmod +x /bin/entrypoint.sh

CMD ["/bin/entrypoint.sh"]
