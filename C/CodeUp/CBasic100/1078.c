/*
 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.


 참고
 while( ) {...}, do {...} while( );, for(...; ...; ...) {...} 등의 반복문은 형태만 다르
 고, 똑같은 성능을 발휘한다. 필요에 따라 편리한 것으로 골라 사용하면 된다.
 */

#include <stdio.h>

int main(void) {
    int n, i, ans=0;
    scanf("%d", &n);
    for (i=0; i<n+1; i++) {
        if (i % 2 == 0) {
            ans += i;
        }
    }
    printf("%d", ans);
}
