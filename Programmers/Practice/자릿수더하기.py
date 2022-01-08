def solution(n):
    answer = 0
    N = str(n)
    for num in N:
        answer += int(num)
    return answer