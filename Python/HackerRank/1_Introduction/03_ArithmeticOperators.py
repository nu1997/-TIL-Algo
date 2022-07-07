def _sum(a, b):
    return a + b

def _diff(a, b):
    return a - b

def _prod(a, b):
    return a * b

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(_sum(a, b))
    print(_diff(a, b))
    print(_prod(a, b))