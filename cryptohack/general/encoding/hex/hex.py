hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# hex diubah ke strings
hex_to_strings = bytes.fromhex(hex)
print("Ini adalah hasil dekripsi dari hex: ", hex_to_strings)

# strings diubah ke hex
strings = bytes.fromhex(hex)
strings_to_hex = bytes.hex(strings)
print("Berikut adalah bentuk hex dari strings diatas: ",strings_to_hex)