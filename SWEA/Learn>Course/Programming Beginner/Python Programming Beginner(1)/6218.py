import sys
sys.stdin = open("ex_016_input.txt")

a = int(input())
for i in range (1, a+1):
    if(a % i == 0):
        print("%d(은)는 %s의 약수입니다." % (i, a))