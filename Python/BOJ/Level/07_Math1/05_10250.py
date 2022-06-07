#ACM호텔
T = int(input())
for tc in range(T):
    h, w, n = map(int, input().split())

    # cnt = 0
    # for i in range(w):
    #     for j in range(h):
    #         cnt += 1
    #         if cnt == n:
    #             ans = str(j+1) + str(i+1).zfill(2)
    #             break;
    # print(ans)

    floor = n % h
    room = n // h + 1

    # 이 부분 캐치를 못한 것 같다. 항상 코드 버전을 남겨두자. 내가 어떻게 생각했는지조차 기억이 안 나 버리면 어떡하라고?
    if floor == 0:
        floor = h
        room -= 1

    print(floor * 100 + room)
    