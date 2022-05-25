# 부녀회장이 될테야
'''
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
'''

'''
# Ver.1 시간초과

def solution(k, n):

    if k == 1:
        return n*(n+1)//2
    if n == 1:
        return 1
    return solution(k-1, n) + solution(k, n-1)


T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    print(solution(k,n))
    
'''

def solution(k, n):
    global matrix
    if matrix[k][n-1] != 0:
        return matrix[k][n-1]
    else:
        matrix[k][n-1] = solution(k, n-1) + solution(k-1, n)
        return matrix[k][n-1]


T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    # 초기화
    matrix = list(list(0 for _ in range(n)) for _ in range(k+1))
    # 기본 규칙 적용
    for i in range(n):
        matrix[0][i] = i+1
    for i in range(k+1):
        matrix[i][0] = 1
    # recursive - memoization
    print(solution(k,n))

''' 다른 사람의 풀이 (반복문)

T = int(input())

for _ in range(T):

    k = int(input()) # 층

    n = int(input()) # 호

    people = [ i for i in range(1, n+1)] #사람수

    for __ in range(k):

        for j in range(1,n):

            people[j] += people[j-1]

    print(people[-1])
    
'''