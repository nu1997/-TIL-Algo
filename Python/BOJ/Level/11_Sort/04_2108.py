# 통계학

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

#N은 홀수

import sys

N = int(sys.stdin.readline().rstrip())
nums = []
mode = dict()
for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))
    try: 
        mode[nums[-1]] += 1
    except:
        mode[nums[-1]] = 1

modes = []

avg = int(round(sum(nums) / N, 0))
med = sorted(nums)[N // 2]
for k, v in mode.items():
    if v == max(mode.values()):
        modes.append(k)
ran = max(nums) - min(nums)
mod = modes[0]
if len(modes) > 1:
    mod = sorted(modes)[1]

print(avg)
print(med)
print(mod)
print(ran)
