def cnt_prime(s, e):
    check = [True] * (e+1)
    m = int(e ** 0.5)
    for i in range(2, m + 1):
        if check[i] == True:
            for j in range(i+i, e, i):
                check[j] = False
    cnt = 0
    for i in range(s, e):
        if i != 1:
            if check[i] == True:
                if str(D) in str(i):
                    cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    ans = cnt_prime(A, B+1)
    print('#%d' % tc, ans)


    # prime_list = [i for i in range(s, e) if check[i] == True]
    # res = []
    # for i in range(len(prime_list)):
    #     if str(D) in str(prime_list[i]):
    #         res.append(prime_list[i])
    # print(res)
    # return len(res)
    # 100개 중 99개 도대체 모가 문제니..