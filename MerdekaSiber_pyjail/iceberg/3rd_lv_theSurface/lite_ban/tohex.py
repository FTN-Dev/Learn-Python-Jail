enc = input('Input character: ')
tempat = []
for c in enc:
    encrypt = hex(ord(c))[1:]
    print(f'\\{encrypt}', end='')

