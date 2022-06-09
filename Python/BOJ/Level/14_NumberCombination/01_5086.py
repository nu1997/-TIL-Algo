def calc(a, b):
    if b % a == 0:
        print('factor')
        return True
    return mul(a, b)

def mul(a, b):
    if a % b == 0:
        print('multiple')
        return True
    print('neither')
    return False

x, y = map(int, input().split())

while x and y:
    calc(x, y)
    x, y = map(int, input().split())