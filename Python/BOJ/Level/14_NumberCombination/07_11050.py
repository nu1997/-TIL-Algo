# 이항 계수란 ?
# - 크기가 n인 유한 집합의 크기가 k인 부분집합의 수
# - nCk = (n k)

# 파스칼의 삼각형
# 구현 (재귀)
# https://rh-tn.tistory.com/32

N, K = map(int, input().split())
ans = 1
for i in range(N, N-K, -1):
    ans *= i
for j in range(K, 0, -1):
    ans //= j
print(ans)