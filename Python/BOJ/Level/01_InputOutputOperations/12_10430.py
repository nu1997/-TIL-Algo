# 나머지

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if 2 <= a <= 10000 and 2 <= b <= 10000 and 2 <= c <= 10000:
    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print((a * b) % c)
    print(((a % c) * (b % c)) % c)
else:
    print('수행 범위를 벗어났습니다.')