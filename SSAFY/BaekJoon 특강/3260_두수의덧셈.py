T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    res = a + b
    print('#%d' % tc, res)