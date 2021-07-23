def solution(n):
    temp = str(n)
    cnt = 0
    flag = True
    if len(temp) > 1:
        standard = int(temp[1]) - int(temp[0])
        for i in range(len(temp)-1):
            if int(temp[i+1]) - int(temp[i]) != standard:
                flag = False
                break
    return flag

N = int(input())
cnt = 0
for i in range(1, N+1):
    if solution(i):
        cnt += 1
print(cnt)