M = int(input())
N = int(input())

l = N - M
sq = int(l ** 0.5)
sieve = [True] * l

for i in range(2, sq):
    if sieve[i] is True:
        for j in range(i+i, l, i):
            sieve[j] = False
print(sieve)