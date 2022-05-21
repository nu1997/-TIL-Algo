// 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.

#include <stdio.h>
int main(void) {
  int a, b;
  scanf("%d %d", &a, &b);
  printf("%d", a%b);
}