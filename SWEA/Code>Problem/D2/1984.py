T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    max_idx = nums.index(max(nums))
    nums.pop(max_idx)
    min_idx = nums.index(min(nums))
    nums.pop(min_idx)
    print('#%d' % tc, round(sum(nums)/len(nums)))