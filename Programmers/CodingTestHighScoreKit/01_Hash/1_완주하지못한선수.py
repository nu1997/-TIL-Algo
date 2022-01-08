# def solution(participant, completion):
#     for complete in completion:
#         participant.remove(complete)
#     answer = str(participant[0])
#     return answer

# def solution(participant, completion):
#     participate_dict = dict()
#     for i in participant:
#         if participate_dict[i]:
#             participate_dict[i] += 1
#         else:
#             participate_dict[i] = 1
#     for j in completion:
#         if participate_dict[j]:
#             if participate_dict[j] > 0:
#                 participate_dict[j] -= 1
#             else:
#                 return j
#         else:
#             continue

# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

# O(n) + O(n) 밖에 없는지 잘 생각해보자

def solution(participant, completion):
    participant_s = sorted(participant)
    completion_s = sorted(completion)
    # print(participant_s, completion_s)
    for i in range(len(completion_s)):
        if participant_s[i] != completion_s[i]:
            return participant_s[i]
    return participant_s[-1]