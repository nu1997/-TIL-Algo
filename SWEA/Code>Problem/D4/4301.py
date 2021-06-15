# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # N X M의 밭에 콩 심기
#     # field = [[1] * N] * M
#     idx = []
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             idx.append((i, j))
#     for i in range(N * M): # 0-5
#         for j in range(i + 1, N * M): # 1 ~ 5 # 2~ 5 # 3~ 6 # 5-5
#             if ((idx[j][1] - idx[i][1]) ** 2 + (idx[j][0] - idx[i][0]) ** 2) ** 0.5 == 2:
#                 # y = idx[j][0]
#                 # x = idx[j][1]
#                 # field[idx[j][1]][idx[j][0]] = 0
#                 cnt += 1
#     ans = N * M - cnt
#     print('#%d %d' % (tc, ans))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [[0] * N] * M
    for 