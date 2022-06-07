# 더하기 사이클

N = input()
if int(N) < 10:
    N = '0' + N
cnt = 1
text = N
while N:
    temp = 0
    for sy in text:
        temp += int(sy)
    if temp < 10:
        temp = '0' + str(temp)
    text = text[-1] + str(temp)[-1]
    if text == N:
        break
    cnt += 1
print(cnt)