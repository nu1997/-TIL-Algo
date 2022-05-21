/*
공백 문자가 포함되어 있는 문장을 입력받고 그대로 출력하는 연습을 해보자.
*/

#include <stdio.h>
int main(){
  char data[2001];
  fgets(data, 2000, stdin);
  printf("%s", data);
}