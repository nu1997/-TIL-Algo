def solution(arr):
    answer = []
    for el in arr:
        if len(answer) == 0:
            answer.append(el)
        else:
            if answer[-1] != el:
                answer.append(el)
    return answer