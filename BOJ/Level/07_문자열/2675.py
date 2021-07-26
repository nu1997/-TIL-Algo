T = int(input())
for _ in range(T):
    R, S = input().split()
    res = ''
    for i in range(len(S)):
        res += S[i] * int(R)
    print(res)