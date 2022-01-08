'''
def solution(priorities, location):
    M = priorities.index(max(priorities))
    if location == M:
        return 1
    a = len([x for x in priorities[:M] if x > priorities[location]])
    b = len([y for y in priorities[M:] if y >= priorities[location]])
    # print(priorities[:M])
    # print(priorities[M:])
    # print(a, b)
    answer = a + b + 1
    return answer
'''
# 큰일났다... 진짜 모르겠다 이게 쉬운거면 어떡하냐고ㅜㅠㅜ....

'''
## 다시 풀어봄 테케 2개 통과
def solution(priorities, location):
    M = priorities.index(max(priorities))
    L = len(priorities)
    # max index로부터 나는 몇 번째?
    key = M - location 
    # 같을 때
    if key == 0:
        return 1
    # 양수일 때 (앞에 있을 때)
    elif key > 0:
        cnt = 0
        for i in range(M):
            if priorities[i] < priorities[location]:
                cnt += 1
        return L - M + 1 - cnt 
    # 음수일 때 (뒤에 있을 때)
    elif key < 0:
        cnt = 0
        for j in range(M, location):
            if priorities[j] < priorities[location]:
                cnt += 1
        return key - cnt
'''

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

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))