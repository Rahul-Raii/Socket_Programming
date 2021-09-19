import socket
s= socket.socket()
print(' Socket Created ')
s.bind(('127.0.0.1',9999))
s.listen(3)
print(' Waiting For The Connection ')
msg='a'
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print(' Connected With ', addr, name)
    while msg!='end':
        msg = c.recv(1024).decode()
        print(' ', msg)
        c.send(bytes(input(('                             ')),'utf-8'))
    c.close()