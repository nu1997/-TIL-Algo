# 벌집
N = int(input())
a = 1
n = 2
if N < 2:
    print(1)
else:
    while True:
        if a + 1 <= N <= a + 6 * (n - 1):
            print(n)
            break
        else:
            a += 6 * (n - 1)
            n += 1
