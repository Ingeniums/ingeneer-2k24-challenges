#!/bin/bash 

socat -dd -T60 tcp-l:1025,reuseaddr,fork exec:'python /app/main.py',pty,stderr

