import socket

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

s.connect("8888")[0]
print(s.recv(1024))

while True:
    you = raw_input()
    data = s.send(you)
    s.recv(1024)
