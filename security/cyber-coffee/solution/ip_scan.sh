#!/bin/bash

subnet="10.69.0"

for octet3 in {1..254}; do
    echo $octet3
    ping -c 1 -w 1 $subnet.$octet3 > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "Host $subnet.$octet3 is up"
    fi
done

