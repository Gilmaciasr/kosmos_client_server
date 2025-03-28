import socket

HOST = '127.0.0.1'
PORT = 5000

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server ready and listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            handle_client(client_socket, client_address)

            client_socket.close()

    except KeyboardInterrupt:
        print("\nServer stopped manually.")
    finally:
        server_socket.close()
        print("Server socket closed.")

def handle_client(client_socket, client_address):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data or data == "DESCONEXION":
                print(f"Client {client_address} connection terminated.")
                break
            print(f"Client message: {data.upper()}")
            client_socket.sendall(data.upper().encode('utf-8'))
        except ConnectionResetError:
            print(f"Client {client_address} connection terminated unexpectedly.")
            break

if __name__ == "__main__":
    start_server(HOST, PORT)