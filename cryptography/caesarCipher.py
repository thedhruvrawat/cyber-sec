def caesar(text, s):
    result=""
    #traversing the plain text
    for i in range(len(text)):
        char = text[i]
        #Encrypt uppercase in plain text
        if(char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)
        #Encrypt lowercase in plain text
        else:
            result+=chr((ord(char)+s-97)%26+97)
    return result

message = 'CAESAR CIPHER DEMO'
shift = 4

print "Plain text: " + message
print "Shift: " + str(shift)
print "Encrypted text: " + caesar(message, shift)

