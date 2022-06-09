import sys

def LCM(x, y):

    def GCD(x, y):
        if x % y == 0:
            return y
        while x % y:
            r = x % y
            return GCD(y, r)
    
    return x * y // GCD(x, y)


T = int(input())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(LCM(a, b))

# 생각보다 input()과 sys.stdin.readline()의 차이가 나니 염두에 둘 것