N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))
for num in sorted(nums):
    print(num)