T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    nbr_list = []
    for i in range(N-M+1):
        nbr_sum = 0
        for j in range(M):
            nbr_sum += numbers[i+j]
        nbr_list += [nbr_sum]
    max_nbr = max(nbr_list)
    min_nbr = min(nbr_list)
    result = max_nbr - min_nbr
    print('#%d %d' % (t, result))

# done.
