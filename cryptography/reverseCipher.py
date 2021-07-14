#Store the message to be encrypted in this variable
message = 'This is a sample reverse cipher program'
encrypted = ''
i = len(message) - 1

while i>=0:
    encrypted = encrypted+message[i]
    i=i-1

print "Encrypted text is: " + encrypted
