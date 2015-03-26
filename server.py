#!/usr/bin/env python
import sys
import socket

if len(sys.argv) < 2:
    print 'Select file to send'
    sys.exit(1)

filename = sys.argv[1]
f = open(filename, 'r')
content = f.read()

sock = socket.socket()
sock.bind(('', 2233))
sock.listen(1)
print 'connected!'
while True:
    connection, address = sock.accept()
    connection.send(content)
    print 'data sent'
    connection.close()


