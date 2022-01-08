def solution(n):
    answer = list(int(x) for x in str(n)[::-1])
    return answer