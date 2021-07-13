def solution(dartResult):
    answer = 0
    game = {'S': 1, 'D': 2, 'T': 3}
    txt = ''
    temp = 0
    queue = []
    top = -1
    for one in dartResult:
        if one.isdigit():
            txt += one
            # temp += int(one)
        elif one in game.keys():
            if txt:
                temp += int(txt)
                txt = ''
            if one.isalpha():
                temp **= game[one]
                queue.append(temp)
                top += 1
                temp = 0
        elif one == '*':
            if top == 0:
                queue[top] *= game[one]
            else:
                queue[top] *= game[one]
                queue[top-1] *= game[one]
        elif one == '#':
            queue[top] *= game[one]
    print(queue)
    answer = sum(queue)
    return answer