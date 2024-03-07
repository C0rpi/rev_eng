#include <stdio.h>
#include <string.h>
#include <sys/random.h>
#include "aes.h"

#define ECB 1


static void phex(uint8_t* str);



int pw_len = 32;
int decrypt(char * input){
  printf("%d\n", strlen(input));
  if (strlen(input) != 32){
    return 0;
  }
  char * password ="12341234123412341234123412341234";
  char * plain_text = input; 
  printf("\n%d\n",strcmp(plain_text,password));
  //printf("\n%s\n",plain_text);
  //printf("%s\n",password);

  uint8_t * key[32];
  printf(*key);
  getrandom(key,32,0);
  printf("key: ");
  phex(key);

  struct AES_ctx ctx;
  AES_init_ctx(&ctx, key);

    for (int i = 0; i < 2; ++i)
    {
      AES_ECB_encrypt(&ctx, plain_text + (i * 16));

    }
  printf("pt: ");
  phex(plain_text);
  printf("0\n");
  struct AES_ctx ctx1;
  printf("1\n");
  AES_init_ctx(&ctx1, key);
  printf("key: ");
  phex(key);
  printf("2\n");

    for (int i = 0; i < 2; ++i)
    {
      AES_ECB_encrypt(&ctx1, &password + (i * 16));
      printf("%d\n",i+3);
    }
  printf("pw: ");
  phex(password);

  return 1;

}

int compare_password(){

  return 1;
}
void main(){
  char* input[pw_len];
  printf("Please enter the password!\n");
  scanf("%s",input);
  /*decrypt the password
   *The Password has to be decrypted at a certain time. But you do not need to save it a one place in the memory 
   */
  if (decrypt(input) == 0){
    printf("NOPENOPE");
  }
  printf("\ending decrypt");
  if(compare_password()==1){
    printf("Right!\n");
  }else{
    printf("False!\n");
  }
}





static void phex(uint8_t* str)
{

#if defined(AES256)
    uint8_t len = 32;
#elif defined(AES192)
    uint8_t len = 24;
#elif defined(AES128)
    uint8_t len = 16;
#endif

    unsigned char i;
    for (i = 0; i < len; ++i)
        printf("%.2x", str[i]);
    printf("\n");
}