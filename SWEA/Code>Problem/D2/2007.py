T = int(input())
for tc in range(1, T+1):
    l = input()
    res = []
    p = 0
    for i in range(1, 11):
        if 30 // i:
            p = 1
        temp = l[0:i] * (30//i + p)
        if l == temp[:30]:
            res += [i]
    print('#%d' % tc, min(res))