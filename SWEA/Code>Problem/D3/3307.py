# 3307. 최장 증가 부분 수열

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_cnt = 0
    cnt = 0
    for i in range(N):
        cnt = 0
        temp = nums[i]
        for j in range(N-i):
            if temp <= nums[i+j]:
                temp = nums[i+j]
                cnt += 1
        if max_cnt <= cnt:
            max_cnt = cnt

    print('#%d %d' % (tc, max_cnt))

