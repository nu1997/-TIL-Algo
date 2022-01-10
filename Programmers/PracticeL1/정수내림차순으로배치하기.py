def solution(n):
    answer = ''
    temp = sorted(list(str(n)), reverse=True)
    for x in temp:
        answer += x
    return int(answer)