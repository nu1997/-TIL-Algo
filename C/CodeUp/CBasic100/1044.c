// 정수를 1개 입력받아 1만큼 더해 출력해보자.

#include <stdio.h>
int main(void) {
  long long int n;
  scanf("%lld", &n);
  n++;
  printf("%lld", n);
}