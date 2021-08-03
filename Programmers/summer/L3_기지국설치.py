import math
def solution(n, stations, w):
    answer = 0
    start = 1
    for station in stations:
        l = station - w - start
        e = w * 2 + 1
        answer += math.ceil(l / e)
        start = station + w + 1
    if start <= n:
        answer += math.ceil((n - start + 1) / e)
    return answer

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))

# import math
# def solution(n, stations, w):
#     answer = 0
#     mini = [0] * n
#     for station in stations:
#         mini[station - (w + 1):station + w] = [1]
#     houses = list(''.join(map(str, mini)).split('1'))
#     for house in houses:
#         if house:
#             l = len(house)
#             e = w * 2 + 1
#             if l <= e:
#                 answer += 1
#             else:
#                 answer += math.ceil(l / e)
#     return answer