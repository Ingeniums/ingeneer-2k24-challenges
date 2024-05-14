import socket

target_host = "10.69.0.17" 

def port_scan(target_host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        s.sendto(b'hello', (target_host, port))
        data, _ = s.recvfrom(1024)
        print(f"Received {len(data)} bytes from {target_host}:{port}: {data.decode()}")
        s.close()
    
    except socket.error as e:
        print(f"Port {port} is closed or filtered")

for port in range(1, 65536):
    port_scan(target_host, port)
