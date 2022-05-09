/*
실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
*/

#include <stdio.h>
int main(){
  float x, y;
  int a, b;
  scanf("%f", &x);
  a = (int) x;
  y = (x - a) * 100000;
  printf("%f", y);
  printf("%d\n%d", a, b);
}