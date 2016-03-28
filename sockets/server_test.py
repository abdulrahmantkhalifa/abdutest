import socket
from _thread import *
import os
host = ''
port = "8888"


os.remove("8888")
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


try:
    s.bind(port)
except socket.error as e:
    print(str(e))

s.listen(5)
print("waiting for connecttion")

def threaded_client(conn):
    conn.send(str.encode("welcome, to hell please enter \n"))

    while True:
        data = conn.recv(1024)
        reply = 'server got' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn, addr = s.accept()
    print("connected to:" + conn.getsockname())
    start_new_thread(threaded_client,(conn,))






