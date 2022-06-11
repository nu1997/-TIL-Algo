# A+B

a, b = input().split()
a = int(a)
b = int(b)
if 0 < a < 10 and 0< b < 10:
    print(a + b)
else:
    print('수행 범위를 벗어났습니다.')