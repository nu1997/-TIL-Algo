# ㅋ.. 정말 더럽네 문제도 뭔말인지 모르갰고... 문제 해석을 대충 감으로...
def solution(A):
    # write your code in Python 3.6
    if A:
        A = sorted(A)
        if A[0] != 1:
            return 1
        for i in range(len(A) - 1):
            if A[i+1] - A[i] > 1:
                return A[i] + 1
        return A[-1] + 1
    return 1

