# Chall
<img src="img/xorkey.png">

## Workflow

As u see at the image of the chall, u can read if the XOR Key is cryptohack flag format and of course its a __crypto__

so im trying with that key and the output is like this

```
b'myXORk}:rVU\x10DFWg)adxE+dQFTX\x0fS[Me$~s\x11EF(euk'
```

u can see if there is readable sentence __myXORk__. But if u use it as the key, the result is not neat, here is the output if u use __myXORk__:

```
b'cryptos1Sis\x14JMvX\x0fejsd\x14BUH_y0u_Cn\x05AU\x15KM\tZSo'
```

damn, its closer to the flag. Back to the first key, __crypto__. But i had some idea, lemme put one by one character of the perfect flag format of cryptohack, __crypto{FLAG}__. Lets try with __crypto{__ first.
Here is the result:

```
b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'
```

damn, u see __myXORke+y__ right? lets try the result with that key:

```
b"crypto{crKX'hfErvwjsd\x14BU@\rX\x12^laE6k,\x07KM\tZSo"
```

closer to the flag, what if we remove the __+__, so it'll be __myXORkey__:

```
b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'
```

and yea, we get the __flag__.