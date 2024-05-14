#!/bin/bash

socat -dd -T60 tcp-l:12345,reuseaddr,fork exec:'python /app/main.py',pty,stderr
