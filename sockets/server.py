import socket

#creating a socket object
s = socket.socket()
print("Socket created successfully")

#reserving a port
port = 42069

#binding to the port
#since no IP will be given, it will listen requests coming from other computers on the network
s.bind(('', port))
print("Socket binded to %s" %(port))

#putting socket into listening mode
s.listen(5)
print("Socket is now listening....")

#an infinite loop till an error occurs or interrupted by user
while True:
    #connect with client
    c, addr = s.accept()
    print("Got a connection from", addr)
    #send thanks to client
    c.send(b"Thanks for connecting")
    #close the connection
    c.close()
