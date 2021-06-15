import sys
sys.stdin = open("ex_026_input.txt")

# 올해는 2021년인데... 2019년으로 세팅되어있자나 ㅠㅠ

name = input()
age = int(input())
year = 2019
x = 2019 - age + 100

print(f'{name}(은)는 {x}년에 100세가 될 것입니다.')