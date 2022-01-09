'''
def solution(n, m):
    answer = []
    n_list = []
    m_list = []
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(i)
    for j in range(1, m+1):
        if m % j == 0:
            m_list.append(j)
    print(n_list, m_list)
    M = max([x for x in n_list if x in m_list])
    L = 1
    for y in list(set(n_list + m_list)):
        L *= y
    answer += [M, L]
    return answer
'''
'''
def key(N):
    key_list = []
    while N > 1:
        for i in range(1, N+1):
            if N % i == 0:
                N //= i
                key_list.append(i)
    return key_list
    
def solution(n, m):
    GCDL = list(x for x in key(n) if x in key(m))

    GCD = 1
    for g in GCDL:
        GCD *= g
    LCM = n * m // GCD
    return [GCD, LCM]
'''

# 유클리드 호제법

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def solution(n, m):
    gcd = GCD(n, m)
    lcm = n * m // gcd
    return [gcd, lcm]

'''
a와 b의 최대공약수는 a를 b로 나눈 나머지 r과 b의 최대공약수와 같다.
'''