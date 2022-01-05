# 10726. 이진수 표현

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    bin_num = bin(M).lstrip('0b').zfill(N)
    # print(bin_num)
    if '0' in bin_num[-N:]:
        res = 'OFF'
    else:
        res = 'ON'
    print('#%d' % tc, res)