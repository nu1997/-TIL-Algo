Y = int(input())
res = 0
if Y % 4 == 0 and Y % 100 != 0:
    res = 1
elif Y % 400 == 0:
    res = 1
print(res)