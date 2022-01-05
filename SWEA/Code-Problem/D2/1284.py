T = int(input())
for tc in range(1, T+1):
    # A기본요금, B기본요금, B기준, B초과요금, W실사용
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if W <= R:
        add = 0
    else:
        add = W - R
    B = Q + (S * add)
    if A > B:
        res = B
    else:
        res = A

    print('#%d' % tc, res)

# done.