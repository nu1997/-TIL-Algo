// 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

#include <stdio.h>

int main(void) {
  int n;
  scanf("%d", &n);
  if (n > 89) {
    printf("A");
  } 
  else if (n > 69) {
    printf("B");
  } 
  else if (n > 39) {
    printf("C");
  } 
  else {
    printf("D");
  }
}