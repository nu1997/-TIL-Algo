# import sys
# sys.stdin

N, M = map(int, input().split())
welcome = "WELCOME"
style = ".|."

cnt = N
while cnt:
    if cnt > N // 2 + 1:
        n = (2 * (N - cnt + 1) - 1)
        m = (M - n * 3) // 2
        res = '-' * m + style * n + '-' * m
    elif cnt == N // 2 + 1:
        m = (M - len(welcome)) // 2
        res = '-' * m + welcome + '-' * m
    elif cnt < N // 2 + 1:
        n = 2 * cnt - 1
        m = (M - n * 3) // 2
        res = '-' * m + style * n + '-' * m
    print(res)
    cnt -= 1