def solution(priorities, location):
    M = priorities.index(max(priorities))
    if location == M:
        return 1
    a = len([x for x in priorities[:M] if x > priorities[location]])
    b = len([y for y in priorities[M:] if y >= priorities[location]])
    # print(priorities[:M])
    # print(priorities[M:])
    # print(a, b)
    answer = a + b + 1
    return answer

# 큰일났다... 진짜 모르겠다 이게 쉬운거면 어떡하냐고ㅜㅠㅜ....