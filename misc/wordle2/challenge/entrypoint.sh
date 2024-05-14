#!/bin/sh

EXEC="./server.py"
PORT=1224

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive, exec:"python3 $EXEC",stderr
