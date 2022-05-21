// 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.

#include <stdio.h>
int main(void) {
  int n;
  scanf("%o", &n);
  printf("%d", n);
}