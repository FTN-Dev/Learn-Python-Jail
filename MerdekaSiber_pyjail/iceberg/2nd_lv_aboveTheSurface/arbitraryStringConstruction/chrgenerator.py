plaintext = input("input plaintext: ")
array = list(plaintext)
for char in array:
    payload = ord(char)
    print(f"chr({payload})+", end='')
