# 입력 없음

my_list = [12, 24, 35, 70, 88, 120, 155]

result = [my_list[i] for i in range(len(my_list)) if i != 0 and i != 4 and i != 5]
print(result)