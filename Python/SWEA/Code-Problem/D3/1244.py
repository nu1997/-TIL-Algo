# 1244. 최대상금

T = int(input())
for C in range(1, T+1):
    N, M = map(int, input().split())
    nums = []
    for i in str(N):
        nums.append(int(i))
    print(nums)
    # for i in range(M): # 0 1
    #     minIdx = len(nums) - 1 - i
    #     temp = len(nums) - 1 - i
    #     for j in range(minIdx-1, -1, -1):
    #         if nums[minIdx] > nums[j]:
    #             minIdx = j
    #     nums[temp], nums[minIdx] = nums[minIdx], nums[temp]
    # print('#%d' % C, end=' ')
    # for num in nums:
    #     print(num, end='')
    # print()
    max_idx = 1
    max_val = 1
    for i in range(M):
        if max_idx == 0:
            
        for j in range(len(nums)):
            if nums[j] > max_val:
                max_val = nums[j]
                max_idx = j
        # max 나와있을 것
        nums[max_idx], nums[i] = nums[i], nums[max_idx]
    print(nums)
