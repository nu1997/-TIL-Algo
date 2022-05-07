T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    check = []
    for i in range(N):
        for j in range(i+1, N):
            if i != j:
                check.append(nums[i] * nums[j])

    for num in check:
        temp = str(num)
        for i in range(len(temp)-1):
            if temp[i] > temp[i+1]:
                break
