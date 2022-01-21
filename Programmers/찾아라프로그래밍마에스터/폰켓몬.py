def solution(nums):
    answer = 0
    x = len(set(nums))
    l = len(nums) // 2
    if l >= x:
        return x
    else:
        return l