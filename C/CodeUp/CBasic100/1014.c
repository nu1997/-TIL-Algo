/*
2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
*/

#include <stdio.h>
int main(){
  char x, y;
  scanf("%c %c", &x, &y);
  printf("%c %c", y, x);
}