#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void
sanitize(const char *str)
{
	for (unsigned long i = 0; i < strlen(str); i++) {
		if (str[i] >= '0' && str[i]<= '9') {
			printf("Illegal character %#02x at offset %#lx\n", str[i], i);
			exit(EXIT_FAILURE);
		}
	}
}

int
main(int argc, char **argv)
{
    unsigned char shellcode[] = {
        //TODO paste your shellcode her
    };

    sanitize(shellcode);
    ((void (*)(void))shellcode)();
	return 0;
}
