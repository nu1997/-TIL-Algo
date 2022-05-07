import sys
sys.stdin = open("ex_038_input.txt")

num = int(input())

for i in range (2, num):
    if num % i == 0:
        result = "소수가 아닙니다"
    else:
        result = "소수입니다."
print(result)