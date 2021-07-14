from string import maketrans

rot13trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

#Translating plain text
def rot13(message):
    return message.translate(rot13trans)

def main():
    text = "ROT13 ALGORITHM IS NOT SAFE"
    print rot13(text)

if __name__ == "__main__":
    main()
