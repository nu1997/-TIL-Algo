T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    goods = [[0, 0] for _ in range(N+1)]
    for _ in range(N):
        V, C = map(int, input().split())
        goods[]