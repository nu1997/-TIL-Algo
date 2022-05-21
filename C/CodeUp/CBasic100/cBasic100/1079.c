/*
 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
 */

#include <stdio.h>

int main(void) {
    char letter;
reload:
    scanf("%c", &letter);
    printf("%c", letter);
    if (letter != 'q'){
        goto reload;
    }
}
