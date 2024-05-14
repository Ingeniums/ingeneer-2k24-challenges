import socket
import time

SERVER_ADDRESS = '10.69.0.17'  
SERVER_PORT = 161

DATA = b"ingeneer{$oM3T1M35_7hE_cOsT_OF_fReE_C0nnECtIV1ty_1S_y0Ur_PRiv4cy}"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        client_socket.sendto(DATA, (SERVER_ADDRESS, SERVER_PORT))
        print(f"Sent {len(DATA)} bytes to {SERVER_ADDRESS}:{SERVER_PORT}")

        # repeat every 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    print("Client shutting down...")
finally:
    print("socket turned off")
    client_socket.close()
