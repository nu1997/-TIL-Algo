def solution(X, Y, D):
    # write your code in Python 3.6
    p = (Y - X) % D
    q = (Y - X) // D
    if p == 0:
        return q
    else:
        return q + 1
