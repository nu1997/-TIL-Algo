# A+B - 7
import sys

for tc in range(1, int(input())+1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d' % (tc, a+b))
