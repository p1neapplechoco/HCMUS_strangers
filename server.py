import socket

def start_server():
    host = '26.81.48.125'  # localhost
    port = 65432        # port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    # if not data:
                    #     break
                    print(f"Received: {data.decode('utf-8')}")
                    response = f"Server received: {data.decode('utf-8')}"
                    conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()