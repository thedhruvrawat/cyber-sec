message = 'GIEWIVrGMTLIVrHIQS'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    decrypted=''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num-key
            if num<0:
                num=num+len(LETTERS)
            decrypted = decrypted+LETTERS[num]
        else:
            decrypted = decrypted+symbol
    print 'Key#' + str(key) + ': ' + decrypted
