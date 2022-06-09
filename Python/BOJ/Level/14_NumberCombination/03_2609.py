def GCD(x, y):
    if x % y == 0:
        return y
    while x % y:
        r = x % y
        return GCD(y, r)

def LCM(x, y):
    return x * y // GCD(x, y)

a, b = map(int, input().split())

print(GCD(a, b))
print(LCM(a, b))