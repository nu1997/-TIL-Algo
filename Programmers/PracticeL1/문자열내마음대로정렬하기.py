def solution(strings, n):
    # 버블 정렬
    for i in range(len(strings)-1, -1, -1):
        for j in range(i):
            # print(i, j, j+1)
            if strings[j][n] > strings[j+1][n]:
                strings[j], strings[j+1] = strings[j+1], strings[j]
            elif strings[j][n] == strings[j+1][n]:
                if strings[j] > strings[j+1]:
                    strings[j], strings[j+1] = strings[j+1], strings[j]
    return strings

# 버블 정렬밖에 기억이 안난다. 효율 좋은 퀵정렬이나 힙정렬도 꼭 공부해서 이 문제를 풀어보자