#!/bin/bash

socat -dd -T60 tcp-l:12345,reuseaddr,keepalive,fork exec:'python /app/main.py',stderr