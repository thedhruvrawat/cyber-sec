def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def encode(key, message):
    order = {
            int(val): num for num, val in enumerate(key)
            }
    cipher = ''
    for index in sorted(order.keys()):
        for part in split_len(message, len(key)):
            try: cipher+=part[order[index]]
            except IndexError: continue
    return cipher

print encode('1234', 'HELLOWORLD')
