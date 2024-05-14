#!/bin/sh





socat tcp-l:1337,reuseaddr,fork,keepalive exec:'python3 ./source.py',stderr