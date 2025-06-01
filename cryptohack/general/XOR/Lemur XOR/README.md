# Chall
<img src="img/lemurxor.png">

## Syntax yang didapatkan

* __from PIL import Image, ImageChops__

    syntax tersebut digunakan untuk memanggil function Image dan ImageChops dari library PIL.

* __Image.Chops.invert()__

    Syntax ini digunakan untuk membalik setiap pixel.

    Contoh:

    ```
    (255, 255, 255) (putih) -> (0, 0, 0) (hitam)
    ```

* __ImageChops.subtract()__

    Syntax ini digunakan untuk mengurangi nilai piksel diantara 2 gambar. Contoh:

    ```
    ImageChops.subtract(i2, i1)
    ```

    maka cara kerjanya kurang lebih akan seperti ini. Contoh:

    ```
    Misalnya: (200, 100, 50) - (100, 100, 50) = (100, 0, 0)
    ```

    Hanya nilai positif yang diambil, dan nilai negatif dianggap 0. Ini berlaku juga pada code berikutnya di file yang sama, yaitu 

    ```
    ImageChops.subtract(i1, i2)
    ```

* __ImageChops.add()__

    Menjumlahkan kedua hasil subtract tadi.


## Workflow

So, for the first, lemme explain about the first code, <a href="lemur1.py">lemur</a>
 