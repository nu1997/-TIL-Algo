# 만약 정확한 값이 필요 없고 값의 대소 관계만 필요하다면, 모든 수를 0 이상 N 미만의 수로 바꿀 수 있습니다. -> 이게 무슨 말일까용

import sys

N = int(input())

''' 시간초과
nums = list(map(int, input().split()))
dist = list(set(nums))

ans = [0] * N

for i in range(N):
    ans[i] = len([num for num in dist if num < nums[i]])

print(*ans)
'''

nums = list(map(int, sys.stdin.readline().split()))
sortnums = sorted(set(nums))
count = {num: idx for idx, num in enumerate(sortnums)}

ans = []
for num in nums:
    ans += [count[num]]
print(*ans)
    