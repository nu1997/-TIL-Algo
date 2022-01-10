def solution(x, n):
    if x == 0:
        return [0] * n
    key = 1 if x > 0 else -1
    answer = list(range(x, x * n + key, x))
    return answer