grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = [[0, 0] for _ in range(N)]
    for i in range(N):
        mid, fin, hw = map(int, input().split())
        scores[i][0] = i + 1
        scores[i][1] = mid * (35 / 100) + fin * (45 / 100) + hw * (20 / 100)

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if scores[j][1] < scores[j+1][1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]

    for i in range(0, N, N//10):
        for j in range(N // 10):
            scores[i+j][1] = grades[i // (N//10)]

    for i in range(len(scores)):
        if scores[i][0] == K:
            print('#%d' % tc, scores[i][1])