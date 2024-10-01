import socket

HOST = "26.81.48.125"  # IP adress server
PORT = 65432        # port is used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print("Client connect to server with port: " + str(PORT))
client.connect(server_address)

try:
    while True:
        msg = input('Client: ')
        if not msg:
            continue
        client.sendall(bytes(msg, "utf8"))
        respond = client.recv(1024)
        print(respond.decode("utf8"))
    # client.sendall(b"This is the message from client")
except KeyboardInterrupt:
    client.close()
finally:
    client.close()

