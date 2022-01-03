# def solution(dirs):
#     # UDLR
#     UDLR = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
#     visited = list()
#     start = [0, 0]
#     for d in dirs:
#         start[0] += UDLR[d][0]
#         start[1] += UDLR[d][1]
#         # https://stackoverflow.com/questions/47311782/python-why-appending-to-a-list-results-in-same-values
#         if start not in visited and -5 <= start[0] <= 6 and -5 <= start[1] <= 5:
#             visited.append(start[:])
#     return len(visited)


def solution(dirs):
    UDLR = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    visited = set()
    x, y = 0, 0
    # dir은 예약어라고 한다...
    for d in dirs:
        dx, dy = UDLR[d]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            go = (x, y, nx, ny)
            x, y = nx, ny
            visited.add(go)
    return len(visited)



print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))