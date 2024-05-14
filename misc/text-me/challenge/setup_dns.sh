#!/bin/bash

MAIN_DOMAIN="ingeniums.club"
SUBDOMAIN="flag"

cat <<EOF > /etc/bind/$MAIN_DOMAIN.zone
\$TTL 86400
@   IN  SOA ns1.$MAIN_DOMAIN. hostmaster.$MAIN_DOMAIN. (
            2018021205 ; Serial
            28800 ; Refresh
            7200 ; Retry
            604800 ; Expire
            86400 ; Minimum TTL
)
@   IN  NS  ns1.$MAIN_DOMAIN.
@   IN  A   127.0.0.1
ns1 IN  A   127.0.0.1
@   IN  TXT "hmmm, flag.ingeniums.club TXT"
EOF

cat <<EOF > /etc/bind/$SUBDOMAIN.$MAIN_DOMAIN.zone
\$TTL 86400
@   IN  SOA ns1.$MAIN_DOMAIN. hostmaster.$MAIN_DOMAIN. (
            2018021205 ; Serial
            28800 ; Refresh
            7200 ; Retry
            604800 ; Expire
            86400 ; Minimum TTL
)
@   IN  NS  ns1.$MAIN_DOMAIN.
@   IN  A   127.0.0.1
ns1 IN  A   127.0.0.1
@   IN  TXT "wel1_D0ne_N0W_YoU_uNdeRsT4nd_W7f_I5_DN5"
EOF

cat <<EOF > /etc/bind/named.conf.local
zone "$MAIN_DOMAIN" {
    type master;
    file "/etc/bind/$MAIN_DOMAIN.zone";
};

zone "$SUBDOMAIN.$MAIN_DOMAIN" {
    type master;
    file "/etc/bind/$SUBDOMAIN.$MAIN_DOMAIN.zone";
};
EOF

named -g -c /etc/bind/named.conf -u bind
