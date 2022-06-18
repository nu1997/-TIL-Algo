# 이항 계수란 ?
# - 크기가 n인 유한 집합의 크기가 k인 부분집합의 수
# - nCk = (n k)

# 파스칼의 삼각형
'''
T = int(input())

for ts in range(1, T+1):
    N = int(input())
    for i in range(N):
        array = [[1] * i for i in range(1, N+1)]
        if i > 1:
            for i in range(N):
                for j in range(i-1, 0, -1):
                    array[i][j] = array[i-1][j-1] + array[i-1][j]

    print('#%d' % ts)
    for i in array:
        print(*i)
'''
# 구현 (재귀)
# https://rh-tn.tistory.com/32

N, K = map(int, input().split())
ans = 1
for i in range(N, N-K, -1):
    ans *= i
for j in range(K, 0, -1):
    ans //= j
print(ans)