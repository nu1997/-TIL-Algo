# 두 수 비교하기

a, b = input().split()
a = int(a)
b = int(b)

if -10000 <= a <= 10000 and -10000 <= b <= 10000:
    if a > b:
        print(">")
    elif a == b:
        print("==")
    else:
        print("<")
else:
    print("수행 범위를 벗어났습니다.")