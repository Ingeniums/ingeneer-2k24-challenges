FROM ubuntu:latest

RUN apt-get update && apt-get install -y bind9

COPY setup_dns.sh /setup_dns.sh

EXPOSE 53/udp

RUN chmod +x /setup_dns.sh

ENTRYPOINT [ "/setup_dns.sh" ]
