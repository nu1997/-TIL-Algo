'''
def solution(s):
    answer = ''
    words = list(s.split())
    for word in words:
        for i in range(len(word)):
            if i % 2:
                answer += word[i].lower()
            else:
                answer += word[i].upper()
        answer += ' '
    return answer.rstrip()

# ^ 위 방법이 아닌이유! 공백이 하나라는 법이 없기 때문이다.
'''

def solution(s):
    answer = ''
    flag = 0
    for char in s:
        if char.isalpha():
            if flag % 2:
                answer += char.lower()
            else:
                answer += char.upper()
            flag += 1
        else:
            answer += char
            flag = 0
    return answer