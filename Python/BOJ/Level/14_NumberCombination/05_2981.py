# 검문

# 나머지가 모두 같아야 한다 ?!
# 숫자는 최대 10 0000 0000 10억. for문 돌릴 수 없음.

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

ans = []
mininum = min(nums)
l = mininum if mininum > 2 else 3
for m in range(2, l):
    temp = []
    flag = 0
    for num in nums: 
        # 나머지
        x = num % m
        if len(temp) == 0:
            temp.append(x)
        else:
            if x != temp[0]:
                flag = 0
                break
            else:
                flag = 1
    if flag == 1:
        ans.append(m)
print(*ans)