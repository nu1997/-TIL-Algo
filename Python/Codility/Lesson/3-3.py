# DP
# 수를 저장해놓고 한칸이 넘어갔을 때 뭐가 되는지 생각?

def solution(A):
    l = len(A)
    memo = [0] * l
    memo[1] = A[0] - sum(A[1:])
    res = abs(memo[1])

    for i in range(1, l - 1):
        memo[i + 1] = memo[i] + (A[i] * 2)
        print(memo[i+1], memo[i])
        if abs(memo[i + 1]) < res:
            res = abs(memo[i + 1])

    return res
