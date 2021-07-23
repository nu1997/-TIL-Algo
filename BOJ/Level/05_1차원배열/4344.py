C = int(input())
for _ in range(C):
    scores = list(map(int, input().split()))
    N = scores[0]
    average = sum(scores[1:]) // N
    cnt = 0
    for i in range(1, N+1):
        if scores[i] > average:
            cnt += 1
    res = cnt / N * 100
    print("{:.3f}%".format(res))