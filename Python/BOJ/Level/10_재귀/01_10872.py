def solution(n):
    global ans
    if n == 1:
        return
    else:
        ans *= n
        solution(n-1)

N = int(input())
ans = 1
solution(N)
print(ans)