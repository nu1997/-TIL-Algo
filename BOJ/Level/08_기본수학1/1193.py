# 분수찾기
N = int(input())
n = 1
while True:
    if n  * (n - 1) // 2 < N <= (n + 1) * n // 2:
        if n % 2:
            # 거꾸로
            x = n*(n+1)//2 - N + 1
        else:
            # 똑바로
            x = N - n*(n-1)//2
        print(f'{x}/{n-(x-1)}')
        break
    else:
        n += 1