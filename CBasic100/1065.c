// 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.

#include <stdio.h>
int main(void) {
  int a[3];
  scanf("%d %d %d", a, a+1, a+2);
  int i;
  for (i=0; i<3; i++) {
    if (a[i] % 2 == 0) {
      printf("%d\n", a[i]);
    }
  }
}