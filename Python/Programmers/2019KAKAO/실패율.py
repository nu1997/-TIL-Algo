# 실패율 나도 실패

def solution(N, stages):
    # 클리어한 사람
    clear = [0] * (N + 1)
    # 도전한 사람
    players = [0] * (N + 1)
    # 실패율
    failure = dict()

    for j in range(1, N + 1):
        for i in range(len(stages)):
            if j < stages[i]:
                clear[j] += 1
            if j <= stages[i]:
                players[j] += 1

    for i in range(1, N+1):
        if players[i] == 0:
            failure[i] = 0
        else:
            failure[i] = (players[i] - clear[i]) / players[i]

    failure_sort = sorted(failure.items(), reverse=True, key=lambda item: item[1])

    answer = []
    for k, v in failure_sort:
        answer += [k]

    return answer

print(solution(4, [2, 2, 2, 2, 2]))


'''
def solution(N, stages):
    user_status = {}
    users = len(stages)
    for stage in range(1, N + 1):
        if users == 0:
            user_status[stage] = 0
            continue
        count = stages.count(stage)
        print(count)
        user_status[stage] = count / users
        users -= count
    return sorted(user_status, key=lambda x: user_status[x], reverse=True)
'''