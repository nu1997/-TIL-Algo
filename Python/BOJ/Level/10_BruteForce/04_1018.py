# 체스판 칠하기
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# print(board)

cnt = 0
for i in range(M - 8 + 1):
    for j in range(N - 8 + 1):
        start = board[i][j]
        print(start, i, j, board[i][j:j+8])
        temp = start
        for p in range(8):
            for q in range(8):
                if temp != board[i+p][j+q]:
                    temp = board[i+p][j+q]:
