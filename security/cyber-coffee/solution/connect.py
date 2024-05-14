import socket

SERVER_ADDRESS = '10.69.0.17'  
SERVER_PORT = 161

DATA = b"hello"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
        client_socket.sendto(DATA, (SERVER_ADDRESS, SERVER_PORT))
        print(f"Sent {len(DATA)} bytes to {SERVER_ADDRESS}:{SERVER_PORT}")

        response, _ = client_socket.recvfrom(1024)
        print("Received data from server:")
        print(response.decode())

except KeyboardInterrupt:
    print("Client shutting down...")
finally:
    print("Socket turned off")
    client_socket.close()
