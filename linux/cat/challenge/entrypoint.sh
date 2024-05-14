#!/bin/bash

rm ~/home/

echo "* * * * * root /bin/rm -f /home/ctf/*" > /etc/cron.d/tmp-cleanup
chmod 0644 /etc/cron.d/tmp-cleanup

crontab /etc/cron.d/tmp-cleanup

service cron start

socat -dd -T60 tcp-l:12345,reuseaddr,fork,su=ctf exec:'/bin/bash -i',pty,stderr
