import sys
sys.stdin = open("ex_034_input.txt")

user1, user2 = input(), input()
p1, p2 = input(), input()

if p1 == p2:
    print("비겼습니다!")
elif (p1 == "가위" and p2 == "보") or (p2 == "가위" and p1 == "보"):
    print("가위가 이겼습니다!")
elif (p1 == "바위" and p2 == "가위") or (p2 == "바위" and p1 == "가위"):
    print("바위가 이겼습니다!")
else:
    print("보가 이겼습니다!")