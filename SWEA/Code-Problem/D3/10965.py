# 제곱수 만들기

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    for i in range(1, N+1):
        if (i ** 2) >= N:
            res = str((i ** 2) / N)
            if res.isdigit():
                res = (i ** 2) // N
                break
    print(res)