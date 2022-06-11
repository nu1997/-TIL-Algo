# 곱셈

a = int(input())
b = input()
if 100 <= a <= 999 and 100 <= int(b) <= 999:
    for i in range(2, -1, -1):
        print(a * int(b[i]))
    print(a * int(b))
else:
    print('세자리 자연수를 입력하세요.')