#!/bin/bash

echo "* * * * * root /bin/rm -f /tmp/*" > /etc/cron.d/tmp-cleanup
chmod 0644 /etc/cron.d/tmp-cleanup

crontab /etc/cron.d/tmp-cleanup

service cron start

printf "Starting server...\n"
python3 /root/server.py  &
printf "Server started\n"
socat -dd -T60 tcp-l:12345,reuseaddr,fork,su=ctf exec:'bash -i',pty,stderr
