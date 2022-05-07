def solution(s):
    try:
        return int(s)
    except:
        if s[0] == '+':
            return int(s[1:])
        else:
            return 0 - int(s[1:])