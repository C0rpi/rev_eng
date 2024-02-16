CC=/usr/bin/gcc
GAS=as
LD=ld
RM=rm
CC_FLAGS=-g -std=c99 -fno-stack-protector -z execstack
ASLR_OFF=/usr/bin/sudo /sbin/sysctl -w kernel.randomize_va_space=0
ASLR_ON=/usr/bin/sudo /sbin/sysctl -w kernel.randomize_va_space=2

.PHONY: all aslr clean

all: shellcode test_shellcode vuln sanitizer

shellcode: shellcode.S
	$(GAS) shellcode.S -o shellcode.o
	$(LD) shellcode.o -o shellcode

test_shellcode: test_shellcode.c
	$(CC) $(CC_FLAGS) -o test_shellcode test_shellcode.c

vuln: vuln.c
	$(CC) $(CC_FLAGS) -o vuln vuln.c
	chown root: $@
	chmod u+s $@

sanitizer: sanitizer.c
	$(CC) $(CC_FLAGS) -o sanitizer sanitizer.c

aslr_off:
	$(ASLR_OFF)

aslr_on:
	$(ASLR_ON)

clean:
	$(RM) *.o shellcode test_shellcode vuln sanitizer
