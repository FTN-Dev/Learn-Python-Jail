from pwn import *

encoded = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
fromhex = bytes.fromhex(encoded)
# print(fromhex)

# trying using strings alphabet
# for c in 'abcdefghijklmnopqrstuvwxyz':
#     kutakpernahikatrambutkulagisemenjakkaubilang = xor(fromhex, c)
#     print(kutakpernahikatrambutkulagisemenjakkaubilang)

# trying using numbers 
for i in range(0, 257):
    kutakpernahikatrambutkulagisemenjakkaubilang = xor(fromhex, i)
    print(f"Xor-ing using number {i}: {kutakpernahikatrambutkulagisemenjakkaubilang}")
    print(f"binary of {i}: {bin(i)[2:]}")
