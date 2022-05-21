/*
다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
*/

#include <stdio.h>
int main() {
  int a, b, c, d, e;
  scanf("%1d%1d%1d%1d%1d", &a, &b, &c, &d, &e);
  printf("[%d]\n", a * 10000);
  printf("[%d]\n", b * 1000);
  printf("[%d]\n", c * 100);
  printf("[%d]\n", d * 10);
  printf("[%d]\n", e);
}