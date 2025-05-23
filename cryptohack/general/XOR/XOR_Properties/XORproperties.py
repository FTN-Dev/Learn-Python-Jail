from pwn import *

# Flow:
# Key1 = Key1
# Key 2 = Key2 ^ Key1
# Key 3 = Key2(new) ^ Key3
# Flag = FLAG ^ KEY1 ^ KEY3(new) ^ KEY2(new)

key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2_xor_KEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY2_xor_KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flag = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key1new = bytes.fromhex(key1)
key2new = xor(bytes.fromhex(KEY2_xor_KEY1), key1new)
key3new = xor(key2new, bytes.fromhex(KEY2_xor_KEY3))
key123_1 = xor(key1new, key3new)
key123_2 = xor(key123_1, key2new)
flagss = xor(bytes.fromhex(flag), key123_2)
print(flagss)




## Under this is practice code, the first code i made.
# key1 = bytes.fromhex(key1)
# key1_2 = bytes.fromhex(KEY2_xor_KEY1)
# key2_3 = bytes.fromhex(KEY2_xor_KEY3)
# flags = bytes.fromhex(flag)

# xor1 = xor(key1_2, key1)
# xor2 = xor(key2_3, xor1)

# keyntah = xor(key1_2, xor2)
# maybflags = xor(flags, keyntah)
# print(maybflags)


