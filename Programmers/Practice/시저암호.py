def solution(s, n):
    answer = ''
    for x in s:
        if x.isalpha():
            key = ord(x) + n
            if 65 <= ord(x) <= 90:
                if key > 90:
                    key -= 26
                answer += chr(key)
            elif 97 <= ord(x) <= 122:
                if key > 122:
                    key -= 26
                answer += chr(key)
        else:
            answer += x
    return answer