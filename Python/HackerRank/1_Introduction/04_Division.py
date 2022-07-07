def _div(a, b):
    return a // b

def _fdiv(a, b):
    return a / b

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(_div(a, b))
    print(_fdiv(a, b))