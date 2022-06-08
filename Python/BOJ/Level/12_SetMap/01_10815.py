# 숫자 카드

import sys

N = int(sys.stdin.readline().rstrip())
check = list(map(int, sys.stdin.readline().split()))
check_dict = {x: 1 for x in check}

M = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().split()))
for card in cards:
    try:
        if check_dict[card]:
            print(1, end=" ")
    except:
        print(0, end=" ")