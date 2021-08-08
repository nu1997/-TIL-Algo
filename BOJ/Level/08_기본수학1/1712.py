# 손익분기점
import math

A, B, C = map(int, input().split())
if C - B > 0:
    x = int(A / (C - B)) + 1
    print(x)
else:
    print(-1)