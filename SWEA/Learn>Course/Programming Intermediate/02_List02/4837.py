def get_subset_num(n, k):
    A = list(range(1, 13))
    l = len(A)
    cnt = 0
    for i in range(1<<l):
        arr = []
        for j in range(l):
            if i & (1<<j):
                arr += [A[j]]
        if len(arr) == n and sum(arr) == k:
            cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())

    print('#%d' % t, get_subset_num(N, K))
