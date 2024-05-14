FROM python:3.11

RUN  apt-get update && apt-get install -y socat

ENV TOTAL_1=18
ENV TOTAL_2=1048576

COPY ./entrypoint.sh /bin/entrypoint.sh

COPY server.py /app/server.py

RUN chmod 700 /bin/entrypoint.sh 

EXPOSE 9090

CMD ["/bin/entrypoint.sh"]