def solution(id_list, report, k):
    user_dict = {user: [[], 0] for user in id_list}
    user_dict_new = {user: 0 for user in id_list}
    for case in report:
        a, b = case.split()
        if a not in user_dict[b][0]:
            user_dict[b][1] += 1
            user_dict[b][0].append(a)
    user_list = list(user_dict.values())
    for log in user_list:
        if log[1] >= k:
            for user in log[0]:
                user_dict_new[user] += 1
    answer = list(user_dict_new.values())
    return answer