T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = 1
    check = [0] * 10
    while 0 in check:
        num_list = [int(i) for i in str(x * N)]
        for num in num_list:
            check[num] += 1
        x += 1
    print('#%d' % tc, (x-1) * N)

# done.