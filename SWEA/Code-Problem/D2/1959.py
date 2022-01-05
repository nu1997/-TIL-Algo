T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_sum = 0
    num_sum = 0

    if N == M:
        for n in range(N):
            num_sum += A[n] * B[n]
        max_sum = num_sum

    elif N > M: # A가 B보다 길 때
            for i in range(N-M+1):
                num_sum = 0
                for j in range(M):
                    num_sum += A[i+j] * B[j]
                if num_sum > max_sum:
                    max_sum = num_sum

    else:
        for i in range(M-N+1):
            num_sum = 0
            for j in range(N):
                num_sum += B[i+j] * A[j]
            if num_sum > max_sum:
                max_sum = num_sum

    print('#%d %d' % (tc, max_sum))