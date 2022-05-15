'''
피보나치 함수

N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
'''

def fibo(n, x, y):

    memo = [0] * (n + 1)
    if n == 1:
        x += 1
        print('x=', x)
        memo[n] = n
        return n
    elif n == 2:
        y += 1
        print('y=', y)
        memo[n] = n
        return n
    else:
        memo[n] = fibo(n-1, x, y) + fibo(n-2, x, y)
        return memo[n]

N = int(input())
a, b = 0, 0
print(fibo(N, a, b))
print(a, b)