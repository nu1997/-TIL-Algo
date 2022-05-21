/*
실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.

만약 실수 부분이 0으로 시작하지 않는다면(예를 들어 1.000009)
scanf("%d.%d", &a, &b)도 하나의 방법이 될 수 있다.
*/

#include <stdio.h>

int main(){
  int a;
  char b[7]; //소수는 6자리 이하
  scanf("%d.%s", &a, b);
  printf("%d\n%s", a, b);
}