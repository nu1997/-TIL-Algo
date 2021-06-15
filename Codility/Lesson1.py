def solution(N):
    # write your code in Python 3.6
    B = format(N, 'b')
    stack = []
    cnt = 0
    flag = 0
    for i in B:
        if i == '1' and flag == 0:
            flag = 1
        elif i == '0' and flag == 1:
            cnt += 1
        elif i == '1' and flag == 1:
            stack.append(cnt)
            cnt = 0
    if stack == []:
        res = 0
    else:
        res = max(stack)
    return res