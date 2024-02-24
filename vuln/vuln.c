#include <stdio.h>
#include <string.h>

void
copy(const char *str)
{
	char buf[256]; 
	strcpy(buf, str); 
	printf("%p\n",buf);
	//printf("(%zd) %s\n", strlen(str), buf);
}

/* entry point */
int
main(int argc, char **argv) 
{
	if (argc < 2) {
		fprintf(stderr, "Usage: %s <string>\n", argv[0]);
		return -1;
	}
	copy(argv[1]);
	return 0;
}
//0x555555555223