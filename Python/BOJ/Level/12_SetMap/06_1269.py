# 대칭 차집합

import sys

A, B = map(int, input().split())
lst_a = list(map(int, sys.stdin.readline().split()))
lst_b = list(map(int, sys.stdin.readline().split()))

full = len(set(lst_a + lst_b))

cnt = 0
if A < B:
    count = {x: 1 for x in lst_a}
    for num in lst_b:
        try:
            if count[num]:
                cnt += 1
        except:
            pass
else:
    count = {x: 1 for x in lst_b}
    for num in lst_a:
        try:
            if count[num]:
                cnt += 1
        except:
            pass

ans = full - cnt
print(ans)

