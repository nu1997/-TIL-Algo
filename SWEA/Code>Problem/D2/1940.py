T = int(input())
for tc in range(1, T+1):
    sec = int(input())
    total = 0
    vel = 0
    command = []
    for i in range(sec):
        command += [input().split()]
    for i in range(sec):
        if command[i][0] == '1':
            vel += int(command[i][1])
        elif command[i][0] == '2':
            vel -= int(command[i][1])
            if vel < 0:
                vel = 0
        total += vel
    print('#%d' % tc, total)