# library
import base64

# decode from hex
ciphertext = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
decode_from_hex = bytes.fromhex(ciphertext)
print("ini adalah hasil dari decode hex ciphertext: ", decode_from_hex)


encode_to_b64 = base64.b64encode(decode_from_hex)
print("ini adalah hasil encode dari decode hex: ", encode_to_b64)