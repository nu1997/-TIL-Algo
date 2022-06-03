N = int(input())
ans = 0
for i in range(N):
    if  N == i + sum(list(int(x) for x in str(i))):
        ans = i
        print(ans)
        break;
else:
    print(ans)