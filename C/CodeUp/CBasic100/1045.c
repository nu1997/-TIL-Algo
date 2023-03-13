// 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.

#include <stdio.h>
int main(void) {
  int a, b;
  scanf("%d %d", &a, &b);
  printf("%d\n%d\n%lld\n%d\n%d\n%.2f", a+b, a-b, a*b, a/b, a%b, (float)a/b);
}
