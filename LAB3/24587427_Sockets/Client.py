

import socket

HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hellow, Server')
    data = s.recv(1024)
   
        print('Received', repr(data))