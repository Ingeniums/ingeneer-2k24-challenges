all infos we need we can get from the linux files system.
    ip addr:
cat /etc/hosts

    MAC address:
cat /sys/class/net/eth0/address

we have python and scapy  already installed.
trying to get the up hosts in the same subnet, we find two, .17 and .23, by scanning both of them for udp servers(tag UDP added in the chall) we found that there is an open port 161 in .17,
by sending random data we received “i’m interested only in receiving the flag, you are not the client I’m interested to receive from”, great we got the thing, this server is waiting for another client to send to it the flag. so obviously we need to achieve arp spoofing attack in order to get the packets which contain the flag that the client continuously send it to the server.