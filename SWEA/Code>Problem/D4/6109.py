def up(arr):
    # 위에서부터 작용 (열 순서)
    for c in range(N): # 0 - 4
        for r in range(N - 1): # 0 - 3
            if r != N - 1 and arr[r][c] == 0:
                for i in range(r+1, N):
                    arr[i][c], arr[i-1][c] = arr[i-1][c], arr[i][c]
            if arr[r][c] == arr[r + 1][c]:
                    arr[r][c] += arr[r][c]
                    arr[r + 1][c] = 0
    # for c in range(N):
    #     for r in range(N - 1):
    #
            # elif arr[r][c] == 0 and r != N - 1:
            #     arr[r][c] = arr[r + 1][c]
            #     arr[r + 1][c] = 0
    return arr


T = int(input())
for tc in range(1, T+1):
    N, S = input().split()
    N = int(N)
    game = [list(map(int, input().split())) for _ in range(N)]
    if S == 'up':
        res = up(game)
    elif S == 'down':
        pass
    elif S == 'left':
        pass
    elif S == 'right':
        pass
    for i in range(N):
        print(*res[i])