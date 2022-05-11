// 1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.

#include <stdio.h>
int main(void) {
  int n;
  scanf("%d", &n);
  printf("%d", !n);
}