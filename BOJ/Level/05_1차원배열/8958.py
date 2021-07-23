T = int(input())
for _ in range(T):
    result = input()
    total = 0
    flag = 0
    for i in result:
        if i == 'O':
            total += (1 + flag)
            flag += 1
        elif i == 'X':
            flag = 0
    print(total)