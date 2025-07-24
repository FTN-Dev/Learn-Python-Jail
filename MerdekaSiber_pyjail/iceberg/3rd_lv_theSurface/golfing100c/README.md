# Golfing 100 Character

u can see at the <a href="blacklist.py">code</a>, it still using LITE ban and u can use more than 100 character.

First, lets use inline for loop to iterate __vars()__ and get the builtins

```
[x for x in vars()]
```

<img src='img/1.png'>

u can see if the __\_\_builtins\_\___ function is on array, so we need to know where is the index of that function. Cuz if we call the function normally, it will make the payload longer.

<img src='img/2.png'>

after that, using this payload will call the __\_\_builtins\_\___ function.

```
[x for x in vars()][6]
```

<img src='img/3.png'>

now lets try to put in inside the __vars()__

<img src='img/4.png'>

now take the __eval()__ and __input()__

<img src='img/5.png'>

it works, now put the __input()__ inside the __eval()__

<img src='img/6.png'>