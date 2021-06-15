import sys
sys.stdin = open("ex_040_input.txt")

# 피보나치 수열 만들기 (재귀함수)
# def Fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     return Fibo(n-1) + Fibo(n-2)


N = int(input())
fibo_list = []

for n in range(N):
    if n == 0:
        fibo_list.append(1)
    elif n == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[n-1]+fibo_list[n-2])

print(fibo_list)