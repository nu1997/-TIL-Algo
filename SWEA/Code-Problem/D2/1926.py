tsn = ['3', '6', '9']

N = int(input())
for i in range(1, N+1):
    res = ''
    clap = 0
    for j in str(i):
        if j in tsn:
            clap += 1
    if clap != 0:
        res += '-' * clap
    else:
        res = str(i)
    print(res, end=' ')


