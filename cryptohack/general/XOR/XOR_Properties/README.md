<p>i will update this readme later, mayb with the explanation of the code. </p>

# Chall
<img src="img/properties.png">

## Syntax yang didapatkan

* __from pwn import *__

Untuk fungsinya disini adalah untuk memanggil semua fungsi yang ada di library pwn, cuma yang akan digunakan disini adalah xor() saja.

* __xor()__

Ini adalah salah satu function yang ada di library pwn, jadi disini fungsinya adalah untuk melakukan perhitungan xor kepada data type apapun, yang dimana dalam kondisi ini adalah

```
xor(bytes, bytes)
```

Untuk yang lain kurang tau bagaimana, apakah bisa string dengan string, atau string dengan int, lain kali akan aku coba.

Tapi ketika mencoba untuk xor biasa menggunakan "^", dibawah ini adalah hasilnya.

```
TypeError: unsupported operand type(s) for ^: 'bytes' and 'bytes'
```

## Workflow
<p>If u see at the image of the chall, u can see if the chall give the clue it self how the code workflow.</p>
