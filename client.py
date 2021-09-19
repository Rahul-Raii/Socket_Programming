import socket
c = socket.socket()
c.connect_ex(('127.0.0.1',9999))
name= input(' Enter your  Name ')
c.send(bytes(name,'utf-8'))
while True:
    msg= input('hy')
    c.send(bytes(msg,'utf-8'))
    print(' ', c.recv(1024).decode())