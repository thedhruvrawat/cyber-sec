import socket

s = socket.socket()

port = 42069

#connects to server on local computer
s.connect(('127.0.0.1', port))

#receive data from server
print(s.recv(1024))

#close connection
s.close()
