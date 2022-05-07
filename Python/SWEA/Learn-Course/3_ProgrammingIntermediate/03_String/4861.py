
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = []
    line = list(input())


    for i in range(N):
        if line[i:M+i] == line[i:M+1][::-1]:
            res = line[i:M+1]
            return res
        array.append(line)

    op_array = []
    op_str = ''
    for i in range(N):
        for j in
    print(array)


