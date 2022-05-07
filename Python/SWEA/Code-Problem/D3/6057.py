
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    AL = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        AL[v1].extend([v2])
        AL[v2].extend([v1])
    cnt = 0
    for i in range(1, N+2):
        for j in range(i+1, N+2):
            for k in range(j+1, N+2):
                if j in AL[i] and k in AL[j] and i in AL[k]:
                    cnt +=1

    print('#%d' % tc, cnt)