T = int(input())
for tc in range(1, T+1):
    D, L, N  = map(int, input().split())
    total_d = 0
    for i in range(N):
        total_d += D * (1 + (i * L / 100))
    print('#%d' % tc, int(total_d))