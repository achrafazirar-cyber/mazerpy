import socket

P1_IP = "192.168.200.29"
P1_PORT = 7001

def send(line: str):
    s = socket.create_connection((P1_IP, P1_PORT), timeout=3)
    s.sendall((line + "\n").encode())
    data = s.recv(1024).decode().strip()
    s.close()
    return data

print(send("COMMIT 1"))
print(send("REVEAL 1"))