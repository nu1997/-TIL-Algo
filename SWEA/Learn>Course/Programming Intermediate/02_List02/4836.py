T = int(input())
for t in range(1, T+1):
    board = [[0] * 10 for i in range(10)]
    N = int(input())
    for n in range(N):
        ar, ac, br, bc, color = map(int, input().split())
        for r in range(ar, br+1):
            for c in range(ac, bc+1):
                board[r][c] += color

    counts = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 3:
                counts += 1

    print('#%d %d' % (t, counts))