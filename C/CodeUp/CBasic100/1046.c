// 정수 3개를 입력받아 합과 평균을 출력해보자.
#include <stdio.h>
int main(void) {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  printf("%lld\n%.1f", a+b+c, (float)(a+b+c)/3);
}