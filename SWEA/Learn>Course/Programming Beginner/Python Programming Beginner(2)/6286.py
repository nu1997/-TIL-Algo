# 입력없음
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

fibo_list = [fibo(i) for i in range(1, 11)]

print(fibo_list)