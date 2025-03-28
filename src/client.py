import socket

HOST = '127.0.0.1'
PORT = 5000

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        handle_message(client_socket)

    except ConnectionRefusedError:
        print("Cannot connect to the server. Please, make sure that the server is up and running.")
    except KeyboardInterrupt:
        print("\nClient stopped manually.")
    finally:
        client_socket.close()
        print("Connection terminated.")

def handle_message(client_socket):
    while True:
        try:
            message = input("Input message --> ")
            client_socket.sendall(message.encode('utf-8'))

            if message == "DESCONEXION":
                client_socket.close()
                print("Disconnected from server...")
                break

            response = client_socket.recv(1024).decode('utf-8')

            if not response:
                print("Server has closed the connection.")
                break

            print(f"Server response: {response}")

        except (BrokenPipeError, ConnectionResetError):
            print("Lost connection to server. Please, make sure the server is up and running.")
            break
        except KeyboardInterrupt:
            print("\nClient stopped manually.")
            break

if __name__ == "__main__":
    start_client(HOST, PORT)
