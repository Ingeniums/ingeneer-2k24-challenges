import socket

HOST = '0.0.0.0' 
PORT = 6969


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    
    server_socket.bind((HOST, PORT))

    server_socket.listen()

    print("Server started on port", PORT)

    while True:
        connection, client_address = server_socket.accept()
        try:
            print("Connection from", client_address)

            connection.sendall(b"ingeneer{7Ry_5CanNIN9_YOUr_oWn_CoMpU7er_MaY8E_Y0u_f!ND_a_door}\n")

        finally:
            connection.close()
