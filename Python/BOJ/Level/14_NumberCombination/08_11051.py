# 이항 계수 2 - 동적 계획법

def binomial(n, k):
    matrix = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if (j == 0 or j == i):
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
    return matrix[n][k]

N, K = map(int, input().split())
ans = binomial(N, K) % 10007
print(ans)
