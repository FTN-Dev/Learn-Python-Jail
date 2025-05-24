# Chall
<img src="img/favorite_byte.png">

## Syntax yang didapatkan

* __bin()__

    syntax bin() digunakan untuk mengubah integer menjadi binary number.

* __[:]__

    [:] syntax ini digunakan untuk __menentukan__ berapa character yang akan diprint atau __menghapus__ berapa character atau huruf yang terletak di awal yang akan diprint, contoh kasusnya ada dibawah ini.

    Contoh untuk menentukan berapa character yang akan diprint:

    ```
    print("Hello World!"[:2])

    output:
    He

    ```

    Contoh untuk menghapus character atau huruf awal yang akan diprint
    
    ```
    print("Hello World!"[2:])

    output:
    llo World!
    ```

## Workflow

If u see at the image of the chall, u can read if the XOR Key is just one byte or 8 bit ( 00000000-11111111 )

 - At first, i forget that one character and one byte is so different, so thats why i try to use all the alphabet character(a-z) for XOR Key, but i was wrong.

 - Second, i still think that one byte was equal one character, so i tried to loop 0,9. But it was wrong again.
    
 - Third, i realize if one byte is 8 bit, so the chance is just using number, bcz 8 bit is just 0-255, and all the alphabet is more than 8 bit.
    - So i tried this loop
        ```
        for i in range(0,257):
        ```
        and make sure 257 is more than 8 bit.
 