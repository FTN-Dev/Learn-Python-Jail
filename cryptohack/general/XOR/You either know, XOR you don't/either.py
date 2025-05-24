from pwn import *

code = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# key = "crypto{"
key2 = "myXORkey"
darihex = bytes.fromhex(code)

xoring = xor(darihex, key2)
print(xoring)