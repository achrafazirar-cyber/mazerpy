import socket
import hashlib

HOST = "0.0.0.0"
PORT = 9000

P1 = ("192.168.200.29", 7001)  
P2 = ("192.168.200.33", 7001)         

def h(x):
    return hashlib.sha256(x.encode()).hexdigest()

def ask(addr, msg):
    s = socket.create_connection(addr)
    s.sendall((msg + "\n").encode())
    data = s.recv(1024).decode().strip()
    s.close()
    return data

def beats(a, b):
    return (a == "pierre" and b == "ciseaux") or \
           (a == "ciseaux" and b == "feuille") or \
           (a == "feuille" and b == "pierre")

def run_round(rnd):
    c1 = ask(P1, f"COMMIT {rnd}").split()[2]
    c2 = ask(P2, f"COMMIT {rnd}").split()[2]

    r1 = ask(P1, f"REVEAL {rnd}").split()
    r2 = ask(P2, f"REVEAL {rnd}").split()

    p1, n1 = r1[2], r1[3]
    p2, n2 = r2[2], r2[3]

    if h(f"{p1}:{n1}") != c1 or h(f"{p2}:{n2}") != c2:
        return "CHEAT DETECTED"

    if p1 == p2:
        return "EGALITE"
    elif beats(p1, p2):
        return "PLAYER1 WINS"
    else:
        return "PLAYER2 WINS"

srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST, PORT))
srv.listen(5)

print("Referee ready on port 9000")

while True:
    c, _ = srv.accept()
    msg = c.recv(1024).decode().strip()
    if msg.startswith("REVEAL"):
        rnd = msg.split()[1]
        result = run_round(rnd)
        c.sendall((result + "\n").encode())
    else:
        c.sendall(b"ERR\n")
    c.close()

