// 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

#include <stdio.h>
int main(void) {
  int data[3];
  scanf("%d %d %d", data, data+1, data+2);
  int i;
  for (i=0; i<3; i++) {
    if (data[i] % 2 == 0) {
      printf("even\n");
    }
    else {
      printf("odd\n");
    }
  }
}