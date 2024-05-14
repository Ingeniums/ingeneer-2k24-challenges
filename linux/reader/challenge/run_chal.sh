#!/bin/bash






socat tcp-l:1337,reuseaddr,fork,keepalive exec:'./out',stderr