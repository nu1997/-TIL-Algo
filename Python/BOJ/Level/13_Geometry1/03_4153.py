a, b, c = map(int, input().split())

while a and b and c:
    lst = sorted([a, b, c])
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        print('right')
    else:
        print('wrong')
    a, b, c = map(int, input().split())
