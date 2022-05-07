import sys
sys.stdin = open("input.txt")

tank = ['<', '>', '^', 'v']

T = int(input())
for tc in range(1, T+1):
    # H * W
    H, W = map(int, input().split())
    game_map = list(list(input()) for _ in range(H))
    N = int(input())
    users = list(input())

    for i in range(H):
        for j in range(W):
            if game_map[i][j] in tank:
                tank_r = i
                tank_c = j

    for user in users:
        if user == 'U':
            game_map[tank_r][tank_c] = '^'
            if tank_r > 0:
                if game_map[tank_r-1][tank_c] == '.':
                    tank_r -= 1
        elif user == 'D':
            game_map[tank_r][tank_c] = 'v'
            if tank_r < H-1:
                if game_map[tank_r+1][tank_c] == '.':
                    tank_r += 1
        elif user == 'L':
            game_map[tank_r][tank_c] = '<'
            if tank_c > 0:
                if game_map[tank_r][tank_c-1] == '.':
                    tank_c -= 1
        elif user == 'R':
            game_map[tank_r][tank_c] = '>'
            if tank_c < W-1:
                if game_map[tank_r][tank_c+1] == '.':
                    tank_c += 1
        else: #S
            if game_map[tank_r][tank_c] == '^':
                if tank_r > 0:
                    temp_r = tank_r - 1
                    while temp_r > 0 and (game_map[temp_r][tank_c] != '#' or game_map[temp_r][tank_c] != '*'):
                        temp_r -= 1
                    if game_map[temp_r][tank_c] == '*':
                        game_map[temp_r][tank_c] = '.'

            elif game_map[tank_r][tank_c] == 'v':
                if tank_r < H-1:
                    temp_r = tank_r + 1
                    while temp_r < H-1 and (game_map[temp_r][tank_c] != '#' or game_map[temp_r][tank_c] != '*'):
                        temp_r += 1
                    if game_map[temp_r][tank_c] == '*':
                        game_map[temp_r][tank_c] = '.'
            elif game_map[tank_r][tank_c] == '<':
                if tank_c > 0:
                    temp_c = tank_c - 1
                    while (temp_c > 0) and (game_map[tank_r][temp_c] != '#' or game_map[tank_r][temp_c] != '*'):
                        temp_c -= 1
                    if game_map[tank_r][temp_c] == '*':
                        game_map[tank_r][temp_c] = '.'
            else: #'>'
                if tank_c < W-1:
                    temp_c = tank_c + 1
                    while (temp_c < W-1) and (game_map[tank_r][temp_c] != '#' or game_map[tank_r][temp_c] != '*'):
                        temp_c += 1
                    if game_map[tank_r][temp_c] == '*':
                        game_map[tank_r][temp_c] = '.'
    print('#%d' % tc)
    # for i in range(W):
    #     print(*(game_map[i]))
    print(game_map)