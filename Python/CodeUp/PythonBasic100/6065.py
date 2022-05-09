'''
3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
'''

nums = list(map(int, input().split()))
for num in nums:
    if num % 2 == 0:
        print(num)