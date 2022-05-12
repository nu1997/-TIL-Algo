### 10진수 -> N진수
def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    
    return rev_base[::-1]