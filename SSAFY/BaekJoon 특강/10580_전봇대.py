TC = int(input())
for tc in range(1, TC+1):
    N = int(input()) # 전선의 개수
    line = []
    for _ in range(N):
        a, b = map(int, input().split())
        line.append((a, b))
    cnt = 0
    # 비교 횟수
    for i in range(N):
        a = line[i][0]
        b = line[i][1]
        # 비교 원본
        for j in range(N):
            x = line[j][0]
            y = line[j][1]
            # 대조군
            if a < x and b > y:
                    cnt += 1
            elif a > x and b < y:
                    cnt += 1
    if cnt > 0:
        cnt //= 2
    print('#%d' % tc, cnt)

