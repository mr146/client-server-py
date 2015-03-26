#!/usr/bin/env python
import socket

sock = socket.socket()
sock.connect(('localhost', 2233))
result = ''
while True:
    data = sock.recv(1024)
    if not data:
        break
    result = result + data
sock.close()
print result
