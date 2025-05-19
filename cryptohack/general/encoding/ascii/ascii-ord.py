flag = "crypto{ASCII_pr1nt4bl3}"

character = list(flag)

ascii_num = []
for c in character:
    num = ord(c)
    ascii_num.append(num)
    # print(ord(c))
print(ascii_num)