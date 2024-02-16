#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <errno.h>
#include <stdint.h>

typedef struct creds creds_t;

typedef struct creds {
	char name[16];
	bool root;
	void (*welcome)(void);
} creds_t;

static creds_t *creds;

/* internal prototypes */
static void
login(void);

static void
s3cr3t(void);


/* entry point */
int
main(int argc, char **argv)
{
	if (argc < 2) {
		printf("usage: %s <name>\n", argv[0]);
		return -1;
	}
	creds = (creds_t *) calloc(1, sizeof(creds_t));
	if (!creds) {
		perror("calloc");
		return -1;
	}

	//XXX
#if 1
	printf("creds = %#lx\n", (uint64_t) creds);
	printf("creds->name = %#lx\n", (uint64_t) &creds->name);
	printf("creds->root = %#lx\n", (uint64_t) &creds->root);
	printf("creds->welcome = %#lx\n", (uint64_t) &creds->welcome);
	printf("login = %#lx\n", (uint64_t) login);
	printf("s3cr3t = %#lx\n", (uint64_t) s3cr3t);
#endif
	//XXX
	creds->welcome = login;
	creds->root = false;
	strcpy(creds->name, argv[1]);
	creds->welcome();
	free(creds);
	return 0;
}


/* internal function definitions */
static void
login(void)
{
	printf("Hello %s, you have %s root privileges.\n", creds->name, ((creds->root) ? "gained" : "no"));
}

static void
s3cr3t(void)
{
	printf("You've gathered secret material!\n");
}
