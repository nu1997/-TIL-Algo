T = int(input())

for ts in range(1, T + 1):
    N = int(input())
    # print(array)
    for i in range(N):
        array = [[1] * i for i in range(1, N + 1)]
        if i > 1:
            for i in range(N):
                for j in range(i - 1, 0, -1):
                    array[i][j] = array[i - 1][j - 1] + array[i - 1][j]

    print('#%d' % ts)
    for i in array:
        print(*i)