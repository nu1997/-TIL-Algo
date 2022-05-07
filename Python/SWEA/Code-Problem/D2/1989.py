T = int(input())
for tc in range(1, T+1):
    s = input()
    if s == s[::-1]:
        res = 1
    else:
        res = 0
    print('#%d' % tc, res)