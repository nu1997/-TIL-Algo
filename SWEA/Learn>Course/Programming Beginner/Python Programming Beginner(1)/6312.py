# 입력없음

def calc_mul(*nums):
    result = 1
    for val in nums:
        if isinstance(val, int) == True:
            result *= val
        else:
            result = '에러발생'
            break
    return result


print(calc_mul(1, 2, '3', 4))
print(calc_mul(1, 2, 3, 4))