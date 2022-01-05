# 사랑의 카운슬러
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    worms = []
    for _ in range(N):
        a, b = map(int, input().split())
        worms.append((a, b))
    V = 10 ** 12
    # for i in range(len(worms)-1):
    #     for j in range(i+1, len(worms)):
    #         temp = ((worms[j][0] - worms[i][0]) ** 2) + ((worms[j][1] - worms[i][1]) ** 2)
    #         if temp < V:
    #             V = temp
    #     # 1 2 3 4
    #     # 12 (34) 13 (24) 14 23 24 34
    # print(V)
    # 6개중에 2개 조합 3개 만들기.