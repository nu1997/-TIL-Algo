def isinstr(str1, str2):
    N = len(str1)  # 5 <= N <= 100
    M = len(str2)  # 100 <= M <= 1000

    for i in range(M - N + 1):
        if str1 == str2[i:i + N]:
            return 1
    return 0


T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()

    print('#%d %d' % (t, isinstr(str1, str2)))
