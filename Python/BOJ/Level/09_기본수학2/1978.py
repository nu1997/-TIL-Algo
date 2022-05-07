N = int(input())
nums = list(map(int, input().split()))
cnt = N

for num in nums:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt -= 1
                break
    else:
        cnt -= 1
print(cnt)