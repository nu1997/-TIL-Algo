# 홍준이

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    # ax + by = 1 부정방정식의 정수해
    for x in range(-b, b+1):
        for y in range(-a, a+1):
            if a*x + b*y == 1:
                res = (x, y)
                break
    if res:
        print('#%d %d %d' % (tc, res[0], res[1]))
    else:
        print('#%d %d' % (tc, -1))