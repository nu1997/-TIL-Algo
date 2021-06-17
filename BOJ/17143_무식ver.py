drc = [[-1, 0], [1, 0], [0, 1], [0, -1]]
R, C, M = map(int, input().split())
# arr = [[0]*C for _ in range(R)]
shark = []

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark = [r, c, s, d, z]
