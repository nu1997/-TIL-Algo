def solution(participant, completion):
    participant_s = sorted(participant)
    completion_s = sorted(completion)
    # print(participant_s, completion_s)
    for i in range(len(completion_s)):
        if participant_s[i] != completion_s[i]:
            return participant_s[i]
    return participant_s[-1]