// 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.

#include <stdio.h>
int main(void) {
  int a, b;
  scanf("%d %d", &a, &b);
  printf("%d", a|b);
}