def no_repeat(my_list):
    my_set = set(my_list)
    modified_list = list(my_set)
    
    print(my_list)
    return modified_list

print(no_repeat([1, 2, 3, 4, 3, 2, 1]))