# 3304. 최장 공통 부분 수열

T = int(input())
for tc in range(1, T+1):
    a, b = input().split()


# 정은교님
# T = int(input())
# for t in range(1, T+1):
#     N, M = input().split()
#     table = [[0]*(len(M)+1) for _ in range(len(N)+1)]
#     for r in range(1, len(N)+1):
#         for c in range(1, len(M)+1):
#             if N[r-1] == M[c-1]:
#                 table[r][c] = table[r-1][c-1]+1
#             else:
#                 table[r][c] = max(table[r-1][c], table[r][c-1])
#     print("#%d %d" % (t, table[-1][-1]))