#g가 공백, b가 별
g, b = 0, 7
while b >=1:
    print("{0}{1}".format(" " * g, "*" * b))
    g += 1
    b -= 2