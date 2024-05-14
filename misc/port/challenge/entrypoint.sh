#!/bin/bash

FLAG="ingeneer{net.iPV4.ip_LOc@L_poRT_R4NG3}"

socat -T60 tcp-l:8005,reuseaddr,fork SYSTEM:"if [ \$SOCAT_PEERPORT -eq 6969 ]; then echo '$FLAG'; else echo 'Your srcPort is: \$SOCAT_PEERPORT'; echo 'i want 00110110001110010011011000111001'; fi" 2>&1 >/dev/null


