for func in __builtins__.__dict__:
    c = list("lite")
    if all(char not in func for char in c):
        print(func)

# __doc__
# abs
# any
# chr
# hash
# max
# ord
# pow
# round
# sum
### vars
# map
# OSError
# IOError
# EOFError
# TabError
# LookupError