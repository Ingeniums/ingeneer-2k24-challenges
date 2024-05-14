#!/bin/bash 


echo 'change-user h4cker & password=nothingagain' >> /home/ctf/.bash_history
socat -dd -T60 tcp-l:1025,reuseaddr,fork,su=ctf exec:'bash -i',pty,stderr

