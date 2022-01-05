# 입력없음

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda x: x % 2 == 0, num_list))
square_list = list(map(lambda x: x ** 2, even_list))

print(square_list)