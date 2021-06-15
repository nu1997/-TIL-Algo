drc = [(1, 0), (0, 1)]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    crossword = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for r in range(N):
        cnt = 0
        for c in range(N):
            if crossword[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0
        if cnt == K:
            total += 1
    for c in range(N):
        cnt = 0
        for r in range(N):
            if crossword[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0
        if cnt == K:
            total += 1
    print('#%d %d' % (tc, total))