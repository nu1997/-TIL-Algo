def solution(A):
    # write your code in Python 3.6
    unpaired = set()
    for el in A:
        if el in unpaired:
            unpaired.remove(el)
        else:
            unpaired.add(el)
    return unpaired.pop()
