def mode(nums):
    for num in nums:
        scores[num] += 1
    m = max(scores)
    max_idx_list = [i for i, v in enumerate(scores) if v == m]
    return max(max_idx_list)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    IntList = list(map(int, input().split()))
    scores = [0] * 101

    print('#%d %d' % (N, mode(IntList)))

# done.