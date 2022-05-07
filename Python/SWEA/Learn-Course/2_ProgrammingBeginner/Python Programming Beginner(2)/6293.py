# 와 어려웠다. 이거는 다시 복습했으면 좋겠음.

import sys
sys.stdin = open("ex_066_input.txt")


def circumference(r):
    circum_r = round(2 * 3.141592 * r, 2)
    return circum_r

r_list = list(map(int, input().split(', ')))
result = [circumference(r) for r in r_list]
stringList = [str(x) for x in result]

print(', '.join(stringList))