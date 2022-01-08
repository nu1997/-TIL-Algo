def solution(x):
    answer = True
    n = 0
    for i in str(x):
        n += int(i)
    if x % n:
        return False
    return answer