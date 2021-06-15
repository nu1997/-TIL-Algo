# 가변형 인자가 아닌데? 뭘까... 2시간동안 삽질했잖아....
def calc_maximum(nums):
    max_num = max(nums)
    return max_num

numbers = 3, 5, 4, 1, 8, 10, 2
print(f'max{numbers} => {calc_maximum(numbers)}')
