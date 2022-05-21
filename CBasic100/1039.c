/*
정수 2개를 입력받아 합을 출력해보자.
단, 입력되는 정수는 -2147483648 ~ +2147483648 이다.

참고
+ 연산자를 사용하면 된다.
단, 계산된 결과가 int 형으로 저장할 수 있는 범위를 넘어갈 수 있기 때문에 다른 데이터형을 사용해야 한다.
*/

#include <stdio.h>
int main(void) {
  long long int a, b;
  scanf("%lld %lld", &a, &b);
  printf("%lld", a+b);
}