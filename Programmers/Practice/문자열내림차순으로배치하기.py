def solution(s):
    answer = ''.join(sorted(s, reverse=True))
    return answer

# list to string
# ''.join(sorted(s, reverse=False))