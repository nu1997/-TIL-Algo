def solution(n):
    phrase = '수박'
    answer = phrase * (n // 2) + phrase[0] * (n % 2)
    return answer