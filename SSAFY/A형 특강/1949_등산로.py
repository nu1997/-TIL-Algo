# 등산로 조성
import sys
sys.stdin = open("1949_input.txt")

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

T = int(input())
for tc in range(1, T+1):
    # 3 ≤ N ≤ 8, 1 ≤ K ≤ 5
    N, K = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    max_list = []
    for r in range(N):
        for c in range(N):
            if my_map[r][c] >= max_val:
                max_val = my_map[r][c]
                max_list.append((r, c))
    max_len = len(max_list)
    for i in range(max_len):
        r, c = max_list[i][0], max_list[i][1]
        visited = list([0] * N for _ in range(N))
        dig = 1
        road = 0
        for j in range(4):
            if r < 0 or temp_r >= N or temp_c < 0 or temp_c >= N:
                break
            temp_r, temp_c = r + drc[j][0], c + drc[j][1]


            my_map[temp_r][temp_c]
            print(my_map[temp_r][temp_c])