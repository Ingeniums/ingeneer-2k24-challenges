FROM ubuntu:latest

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssh-server systemd rsyslog

RUN useradd -s /bin/bash ingeneerZombie \
    && echo 'ingeneerZombie:ingeneeeeeer125445' | chpasswd 

RUN mkdir /home/ingeneerZombie \
    && chown ingeneerZombie:ingeneerZombie /home/ingeneerZombie
COPY flag.txt /
RUN chmod 444 /flag.txt 
COPY access.log /var/log/nginx/access.log
RUN rm /usr/bin/scp
RUN chmod go-rx /usr/bin/passwd /usr/bin/ssh 
# COPY sshd_config /etc/ssh/sshd_config
# /usr/bin/cd
ENTRYPOINT service ssh start \
    && tail -f --retry /var/log/auth.log