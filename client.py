import socket

def start_client():
    host = '26.81.48.125'  # The server's hostname or IP address
    port = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            message = input("Enter a message to send (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break

            s.sendall(message.encode('utf-8'))
            data = s.recv(1024)
            print(f"Received from server: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_client()