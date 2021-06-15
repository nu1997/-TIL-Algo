def find_number(my_list, num):
    if num in my_list:
        return (f'{num} => True')
    else:
        return (f'{num} => False')


print([2, 4, 6, 8, 10])
print(find_number([2, 4, 6, 8, 10], 5))
print(find_number([2, 4, 6, 8, 10], 10))