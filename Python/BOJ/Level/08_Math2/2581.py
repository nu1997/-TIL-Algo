
'''
l = N - M
sq = int(l ** 0.5)
sieve = [True] * l

for i in range(2, sq):
    if sieve[i] is True:
        for j in range(i+i, l, i):
            sieve[j] = False
print(sieve)
'''

M = int(input())
N = int(input())

nums = []

# 1은 소수가 아니다... OTL
if M < 2:
    M = 2

for i in range(M, N+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break;
    else:
        nums.append(i)

if nums:
    print(nums)
    print(sum(nums))
    print(nums[0])
else: print(-1)