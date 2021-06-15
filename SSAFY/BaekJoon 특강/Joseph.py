T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    circle = list(range(1, N+1))
    array = []
    i = 2
    while circle:
        while i >= (N-len(array)):
            i -= len(circle)
        array.append(circle.pop(i))
        i += 2
    print(array[-1])