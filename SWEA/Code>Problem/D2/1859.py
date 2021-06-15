T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))[::-1]
    total = 0
    max_price = price[0] # 맨뒤값
    for i in range(1, N):
        if price[i] > max_price:
            max_price = price[i]
        else:
            total += max_price - price[i]

    # 앞에서부터 순회 - 시간초과
    # rice = list(map(int, input().split()))
    # l = len(price)
    # total = 0
    # for i in range(l-1):
    #     prof = 0
    #     for j in range(i+1, l):
    #         if (price[j] - price[i]) > prof:
    #             prof = price[j] - price[i]
    #     total += prof
    print('#%d' % tc, total)