#!/bin/bash

umask 077

echo "* * * * * root /bin/rm -f /tmp/*" > /etc/cron.d/tmp-cleanup

chmod 0644 /etc/cron.d/tmp-cleanup

crontab /etc/cron.d/tmp-cleanup

service cron start

socat -dd -T60 tcp-l:1025,reuseaddr,fork,su=ctf exec:'bash -i',pty,stderr

