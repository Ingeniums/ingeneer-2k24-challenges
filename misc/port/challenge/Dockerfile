FROM python:3.11

RUN apt-get update && apt-get install -y socat

WORKDIR /app

COPY entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]
