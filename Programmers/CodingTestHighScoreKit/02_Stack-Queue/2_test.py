def solution(priorities, location):
    cnt_list = [0] * 10
    queue = []
    for prior in priorities:
        cnt_list[prior-1] += 1
    pointer = max(priorities)
    sorted_list = sorted(priorities)
    while priorities:
        # print(cnt_list)
        if cnt_list[priorities[0]] == 0:
            x = priorities.pop(0)
            print(x)
            queue.append(x)
            cnt_list[x-1] -= 1
        else:
            priorities.append(priorities.pop(0))
            
    print(cnt_list)
    print(queue)
    
    answer = 0
    return answer

# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))