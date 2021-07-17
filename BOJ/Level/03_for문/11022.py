# A+B - 8

import sys

for tc in range(1, int(input())+1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d' % (tc, a, b, a+b))
