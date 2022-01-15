def solution(sizes):
    a_list = []
    b_list = []
    for size in sizes:
        a = size[0]
        b = size[1]
        if a > b:
            a, b = b, a
        a_list.append(a)
        b_list.append(b)
    return max(a_list) * max(b_list)