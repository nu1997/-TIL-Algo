N = int(input())
nums = list(map(int, input().split()))

print(sum(nums) / N * 100 / max(nums))