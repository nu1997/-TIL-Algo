def solution(a,k):
    if a == 0:
        return k
    elif a == 1:
        return k*(k+1)//2
    return solution(a-1,k) + solution(a,k-1)


T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    print(solution(k,n))