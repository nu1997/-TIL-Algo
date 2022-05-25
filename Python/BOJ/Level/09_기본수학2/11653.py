import math

N = int(input())

'''효율성 극악 Greedy
div = 2
while N > 1:
    if N % div == 0:
        N //= div
        print(div)
    else:
        div += 1
'''

primes = []
for i in range(N+1):
    for j in range(2, int(math.sqrt(N))+1):
        if i % j == 0:
            break;
    else:
        primes.append(i)

print(primes)
# while N > 1: