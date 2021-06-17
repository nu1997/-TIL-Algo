drc = [[-1, 0], [1, 0], [0, 1], [0, -1]]

R, C, M = map(int, input().split())
arr = [[0]*C for _ in range(R)]
# 전체 격자판 중에서 이동할 상어가 있는 좌표만 담는 집합. 즉, 이후에 상어의 좌표로만 연산을 하기 위함
shark_set = set()
# 이동을 마친 상어들 중 다음 턴에서 낚시왕이 서있는 열에 있게 되는 상어들의 행 집합.
target_shark = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    # 상어가 도는 싸이클이 생긴다. 싸이클의 나머지 만큼만 이동하면 된다.
    # 상하로 움직이면 ((R-1)*2)가 싸이클, 좌우로 움직이면 ((C-1)*2)가 싸이클
    if d in {1, 2}:
        arr[r-1][c-1] = [s % ((R-1)*2), d-1, z]
    else:
        arr[r-1][c-1] = [s % ((C-1)*2), d-1, z]
    shark_set.add((r-1, c-1))
    if c-1 == 0:
        target_shark.append(r-1)

result = 0
# 이 for문이 낚시왕이 각 열을 방문하게 되는 것
for i in range(C):
    # 낚시왕이 해당 열에 서서 땅에서 가장 가까운 상어를 낚는 과정
    if target_shark:
        min_r = R
        for r in target_shark:
            if r < min_r:
                min_r = r

        result += arr[min_r][i][2]
        shark_set.remove((min_r, i))
    target_shark = []
    temp_shark_set = set()
    # 격자판을 새로운 격자판 위에서 해야하는 이유 -> 코드 상에서는 상어들을 동시에 움직일 수가 없다.
    # 따라서, 이동을 마친 상어의 정보와 이동을 아직 하지 않은 상어의 정보가 동시에 존재 -> 충돌하지 않게 하기 위해 새로운 격자판 생성
    new_arr = [[0]*C for _ in range(R)]
    for r, c in shark_set:
        s, d, z = arr[r][c]
        nr, nc = r, c
        for _ in range(s):
            # 가장자리에 갔을 때 방향 전환
            if nr == R-1 and d not in {2, 3}:
                d = 0
            elif nr == 0 and d not in {2, 3}:
                d = 1
            if nc == C-1 and d not in {0, 1}:
                d = 3
            elif nc == 0 and d not in {0, 1}:
                d = 2
            # 방향에 따라 이동
            dr, dc = drc[d]
            nr += dr
            nc += dc
        # 상어의 이동이 끝나면 새로운 격자판에 상어 정보 표시
        if not new_arr[nr][nc]:
            new_arr[nr][nc] = [s, d, z]
            temp_shark_set.add((nr, nc))
            if nc == i+1:
                target_shark.append(nr)
        else:
            if new_arr[nr][nc][2] < z:
                new_arr[nr][nc] = [s, d, z]
    # 이제 new_arr을 기존의 격자판에 넣어줌. deepcopy
    arr = [list(row) for row in new_arr]
    shark_set = temp_shark_set

print(result)