def solution(s):
    check = [0, 0]
    for char in s:
        if char == 'p' or char == 'P':
            check[0] += 1
        elif char == 'y' or char == 'Y':
            check[1] += 1
    if check[0] == check[1]:
        return True
    else:
        return False