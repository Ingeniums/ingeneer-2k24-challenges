FROM python:3.11

RUN apt update && apt install -y socat 

RUN useradd ctf

COPY entrypoint.sh /bin/entrypoint.sh

COPY out /.here/out

RUN chmod 555 /.here/out

COPY prog.c /.here/prog.c

RUN chmod 444 /.here/prog.c 

COPY flag.txt /flag.txt

RUN chmod +x /bin/entrypoint.sh

RUN chown root:root /flag.txt

RUN chmod 700 /flag.txt

RUN chown root:root /.here/out

RUN chmod u+s /.here/out

ENTRYPOINT ["/bin/entrypoint.sh"]
