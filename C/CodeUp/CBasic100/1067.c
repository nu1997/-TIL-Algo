// 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

#include <stdio.h>
int main(void) {
  int n;
  scanf("%d", &n);
  if (n>0) {
    printf("plus\n");
    if (n%2) {
      printf("odd\n");
    } else {
      printf("even\n");
    }
  }
  else {
    printf("minus\n");
    if (n%2) {
      printf("odd\n");
    } else {
      printf("even\n");
    }
  }
}