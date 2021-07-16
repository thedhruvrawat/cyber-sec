import math, pyperclip

def main():
    message = 'Cenoonommstmme oo snnio. s s c'
    key = 8
    plaintext = decryptTransposition(key, message)
    print(plaintext+'|')
    pyperclip.copy(plaintext)

def decryptTransposition(key, message):
    numCol = math.ceil(len(message)/key)
    numRow = key
    numShadedBoxes = (numCol*numRow) - len(message)
    plaintext = ['']*numCol
    col = 0
    row = 0
    for symbol in message:
        plaintext[col]+=symbol
        col+=1
        if (col==numCol) or (col==numCol-1 and row>=numRow-numShadedBoxes):
            col = 0
            row+=1
    return "".join(plaintext)

if __name__ == "__main__":
    main()
