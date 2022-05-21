// 영문자 1개를 입력받아 그 다음 문자를 출력해보자.

#include <stdio.h>
int main(void) {
  char a;
  scanf("%c", &a);
  printf("%c", a+1);
}