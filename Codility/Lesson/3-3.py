def solution(A):
    # write your code in Python 3.6

    l = len(A)
    ans = 987654321
    for i in range(1, l):
        temp = abs(sum(A[:i]) - sum(A[i:]))
        if temp < ans:
            ans = temp
    return ans