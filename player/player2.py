import socket
import threading
import secrets
import hashlib
import random

HOST = "0.0.0.0"
PORT = 7001
CHOICES = ["pierre", "feuille", "ciseaux"]
state = {}

def h(x):
    return hashlib.sha256(x.encode()).hexdigest()

def handle(conn):
    data = conn.recv(1024).decode().strip().split()
    if len(data) < 2:
        conn.close()
        return

    cmd, rnd = data[0], data[1]

    if cmd == "COMMIT":
        choice = random.choice(CHOICES)
        nonce = secrets.token_hex(8)
        digest = h(f"{choice}:{nonce}")
        state[rnd] = (choice, nonce, digest)
        conn.sendall(f"COMMIT {rnd} {digest}\n".encode())

    elif cmd == "REVEAL":
        choice, nonce, digest = state[rnd]
        conn.sendall(f"REVEAL {rnd} {choice} {nonce}\n".encode())

    conn.close()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)

print("Player2 actif sur le port 7001")

while True:
    c, _ = s.accept()
    threading.Thread(target=handle, args=(c,), daemon=True).start()
