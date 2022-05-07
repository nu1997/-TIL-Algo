ones = [1, 3, 5, 7, 8, 10, 12]
zeros = [4, 6, 9, 11]

T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    ans = 0
    ans += d2
    if m2 - m1 > 0:
        for m in range(m1+1, m2):
            if m == 2:
                ans += 28
            elif m in ones:
                ans += 31
            else:
                ans += 30
        if m1 == 2:
            ans += (28 - d1 + 1)
        elif m1 in ones:
            ans += (31 - d1 + 1)
        elif m1 in zeros:
            ans += (30 - d1 + 1)

    print('#%d' % tc, ans)