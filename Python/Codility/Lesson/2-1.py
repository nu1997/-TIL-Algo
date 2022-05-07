def solution(A, K):
    # write your code in Python 3.6
    l = len(A)
    C = K % l
    if C == 0:
        return A
    else:
        res = A[l-C:] + A[0:l-C]
        return res