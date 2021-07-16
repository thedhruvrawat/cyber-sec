import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("SOCKET successfully created!")
except socket.error as err:
    print("SOCKET CREATION FAILED with error %s" %(err))

#Set default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror: #If host not resolved
    print("There was an error resolving the host :/")
    sys.exit()

#Connect to server
s.connect((host_ip, port))

print("Socket successfully connected to google.com on port = %s" %(host_ip))
