# 입력없음

my_list = [12, 24, 35, 70, 88, 120, 155]

# 인덱스는 0부터지만 홀수번째 항목이란 = 인덱스 항목이 짝수라는 점
result = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]
print(result)