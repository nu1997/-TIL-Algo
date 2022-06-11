# 사칙연산

a, b = input().split()
a = int(a)
b = int(b)
if 1 <= a <= 10000 and 1 <= b <= 10000:
    print(a + b)
    print(a - b)
    print(a * b)
    print(int(a / b))
    print(a % b)
else:
    print('수행 범위를 벗어났습니다.')