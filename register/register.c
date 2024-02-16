#include<stdio.h>
#include<stdlib.h>

void banner(){
  puts("\x1b[35m  ____  _____ ____  _____  _____  \x1b[0m");
  puts("\x1b[35m / ___\\/  __//   _\\/__ __\\/    / \x1b[0m");
  puts("\x1b[35m |    \\|  \\  |  /    / \\  |  __\\ \x1b[0m");
  puts("\x1b[35m \\___ ||  /_ |  \\__  | |  | |    \x1b[0m");
  puts("\x1b[35m \\____/\\____ \\____/  \\_/  \\_/     \x1b[0m");
  puts("\x1b[35m   \x1b[0m");
  return;
}

void setup(){
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  return;
}

void reg(){
  char local_58 [80];

  printf("[\x1b[34mi\x1b[0m] Initialized attendee listing at %p.\n",local_58);
  puts("[\x1b[34mi\x1b[0m] Starting registration application.\n");
  printf("Hacker name > ");
  gets(local_58);
  puts("\n[\x1b[32m+\x1b[0m] Registration completed. Enjoy!");
  puts("[\x1b[32m+\x1b[0m] Exiting.");
  return;
}

int main(){
    setup();
    banner();
    reg();
    return 0;
}
