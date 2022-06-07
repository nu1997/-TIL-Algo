# 체스판 칠하기
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

ans = 987654321
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        cnt_1, cnt_2 = 0, 0
        start = board[i][j]
        # print(start, i, j, board[i][j:j+8])
        other = 'B' if start == 'W' else 'W'
        for p in range(8):
            for q in range(8):
                if (p % 2) ^ (q % 2):
                    if board[i+p][j+q] != start:
                        cnt_1 += 1
                else:
                    if board[i+p][j+q] != other:
                        cnt_1 += 1
        for r in range(8):
            for s in range(8):
                if (r % 2) ^ (s % 2):
                    if board[i+r][j+s] != other:
                        cnt_2 += 1
                else:
                    if board[i+r][j+s] != start:
                        cnt_2 += 1
        cnt = cnt_1 if cnt_1 < cnt_2 else cnt_2
        if cnt < ans:
            # print(i, j)
            ans = cnt
print(ans)
