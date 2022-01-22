nums = {1: '1', 2: '2', 3: '4'}
def solution(n):
    answer = ''
    while n > 3:
        answer += nums[n % 3]
        n //= 3
    answer += nums[n // 3]
    return answer

# print(solution(1))