# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 에라토스테네스의 체

M, N = map(int, input().split())

l = N + 1
sq = int(l ** 0.5)
sieve = [1] * l

for i in range(2, sq+1):
    if sieve[i] == 1:
        for j in range(i+i, l, i):
            sieve[j] = 0

sieve[0], sieve[1] = 0, 0

for i, val in enumerate(sieve[M:]):
    if val == 1:
        print(i+M)