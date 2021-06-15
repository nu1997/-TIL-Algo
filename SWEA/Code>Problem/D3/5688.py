# 세제곱근을 찾아라

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = -1
    for i in range(10**6+1):
        if i ** 3 == N:
            ans = i
            break
    print('#%d %d' % (tc, ans))