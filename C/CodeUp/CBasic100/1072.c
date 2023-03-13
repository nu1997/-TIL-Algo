/*
n개의 정수가 순서대로 입력된다.
-2147483648 ~ +2147483647, 단 n의 최대 개수는 알 수 없다.

n개의 입력된 정수를 순서대로 출력해보자.

while( ), for( ), do~while( ) 등의 반복문을 사용할 수 없다.
*/

#include <stdio.h>


int main(void) {
  int tc, n;
  scanf("%d", &tc);
  reload:
    scanf("%d", &n);
    printf("%d\n", n);
    if (--tc > 0) goto reload;
}