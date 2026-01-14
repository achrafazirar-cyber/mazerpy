import socket

HOST = "0.0.0.0"
PORT = 9000

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print("Referee actif sur le port 9000")

while True:
    conn, addr = s.accept()
    msg = conn.recv(1024).decode().strip()
    print("Message reçu :", msg)
    conn.sendall(b"OK\n")
    conn.close()
