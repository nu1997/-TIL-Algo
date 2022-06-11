# 사분면 고르기

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        res = 1
    else:
        res = 4
else:
    if y > 0:
        res = 2
    else:
        res = 3
print(res)