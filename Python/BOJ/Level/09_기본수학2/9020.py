# 골드바흐의 추측
'''
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
'''

# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것

''' 시간 초과
T = int(input())

for tc in range(T):
    N = int(input())
    # 소수 리스트 구하기
    l = N + 1
    sq = int(l ** 0.5)
    sieve = [1] * l
    for i in range(2, sq+1):
        if sieve[i] == 1:
            for j in range(i+i, l, i):
                sieve[j] = 0
    p_nums = []
    for i, val in enumerate(sieve):
        if val == 1 and i > 1:
            p_nums.append(i)
    # 완전탐색 - 시간초과
    m = len(p_nums)
    x, y = N, N*2
    for i in range(m-1):
        for j in range(i, m):
            if p_nums[i] + p_nums[j] == N:
                if p_nums[j] - p_nums[i] < y - x:
                    x, y = p_nums[i], p_nums[j]
    print(x, y)
'''

# 소수 리스트 구하기 - 효율 좋지 않다.
maximum = 10000
l = maximum + 1
# sq = int(l ** 0.5)
sieve = [1] * l
p_nums = []
for i in range(2, l):
    if sieve[i] == 1:
        p_nums.append(i)
        for j in range(i+i, l, i):
            sieve[j] = 0

def prime(n):
    if n == 1:
        return False
    sq = int(n**0.5)
    for i in range(2, sq+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for tc in range(T):
    N = int(input())
    x, y = N // 2, N // 2
    while True:
        if prime(x) and prime(y):
            break;
        x -= 1
        y += 1
    print(x, y)



