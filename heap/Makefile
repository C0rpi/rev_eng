CC=gcc
CFLAGS= -std=gnu99 -D_GNU_SOURCE
#CFLAGS= -pie -fPIE -std=gnu99 -D_GNU_SOURCE
OBJ = heap.o
RM = rm -rf
TARGETS = heap
ASLR_ON=/usr/bin/sudo /sbin/sysctl -w kernel.randomize_va_space=2
ASLR_OFF=/usr/bin/sudo /sbin/sysctl -w kernel.randomize_va_space=0

all: $(TARGETS)

.c.o:
	$(CC) $(CFLAGS) -c $<

aslr_on:
	$(ASLR_ON)

aslr_off:
	$(ASLR_OFF)

clean:
	$(RM) $(OBJ) $(TARGETS)

.PHONY: all clean
