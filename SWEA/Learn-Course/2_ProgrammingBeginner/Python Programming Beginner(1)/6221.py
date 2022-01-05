import sys
sys.stdin = open("ex_022_input.txt")

a = input()
b = input()
lst = ["가위", "바위", "보"]
result = "잘못된 입력입니다"

#a가 가위인 경우
if a == lst[0]:
    #b가 낸 것에 의해 결정
    if b == lst[0]:
        result = "Result : Draw"
    elif b == lst[1]:
        result = "Result : Man2 Win!"
    elif b == lst[2]:
        result = "Result : Man1 Win!"
elif a == lst[1]:
    if b == lst[0]:
        result = "Result : Man1 Win!"
    elif b == lst[1]:
        result = "Result : Draw"
    elif b == lst[2]:
        result = "Result : Man2 Win!"
elif a == lst[2]:
    if b == lst[0]:
        result = "Result : Man2 Win!"
    elif b == lst[1]:
        result = "Result : Man1 Win!"
    elif b == lst[2]:
        result = "Result : Draw"
print(result)