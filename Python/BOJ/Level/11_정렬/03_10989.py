# 카운팅 정렬 메모리 초과
N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))
limit = max(nums) + 1

count = [0] * limit
# check = [0] * limit
ans = [0] * N

for num in nums:
    # check[num] += 1
    while num < limit:
        count[num] += 1
        num += 1

for i in range(N-1, -1, -1): #987654321
    count[nums[i]] -= 1
    ans[count[nums[i]]] = nums[i]

for num in ans:
    print(num)

