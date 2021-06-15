# 입력 없음

def no_repeat(num_list):
    new_list = []
    for num in num_list:
        if num not in new_list:
            new_list.append(num)

    return new_list

my_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

print(no_repeat(my_list))