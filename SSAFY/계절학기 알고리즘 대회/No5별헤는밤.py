T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    sky = [[0] * N] * N
    for i in range(M):
        r, c, br = map(int, input().split())
        for j in range(br + 1):
            sky[r-br][c]
    print(sky)