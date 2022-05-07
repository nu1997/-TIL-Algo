def solution(n, lost, reserve):
    answer = 0
    check = [1] * n
    for student in lost:
        check[student-1] -= 1
    for student in reserve:
        check[student-1] += 1
    for i in range(n):
        if check[i] == 0:
            try:
                if i > 0:
                    if check[i-1] > 1:
                        check[i-1] -= 1
                        check[i] += 1
                    elif check[i+1] > 1:
                        check[i+1] -= 1
                        check[i] += 1
                    else:
                        continue
                else:
                    if check[i+1] > 1:
                        check[i+1] -= 1
                        check[i] += 1
                    else:
                        continue
                    
            except:
                pass
    for num in check:
        if num >= 1:
            answer += 1
    return answer