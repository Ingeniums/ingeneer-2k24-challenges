FROM python:3.11

RUN  apt-get update && apt-get install -y socat

RUN useradd -m -s /bin/bash ctf

RUN echo 'ctf:ctfctfctf' | chpasswd

COPY ./entrypoint.sh /bin/entrypoint.sh

COPY server.py /app/server.py

RUN chmod 700 /bin/entrypoint.sh 

EXPOSE 9090

CMD ["/bin/entrypoint.sh"]