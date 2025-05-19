import base64

plaintext = "Aku suka b64"
encode = base64.b64encode(plaintext.encode('utf-8'))
print("ini adalah hasil encode: ",encode)

ciphertext = "QWt1IHN1a2EgYjY0"
decode = base64.b64decode(ciphertext.encode('utf-8'))
print('ini adalah hasil decode: ',decode)