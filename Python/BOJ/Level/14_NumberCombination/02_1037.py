N = int(input())
factors = list(map(int, input().split()))
factors.sort()
l = len(factors)
if l % 2:
    print(factors[l // 2] ** 2)
else:
    print(factors[0] * factors[-1])
