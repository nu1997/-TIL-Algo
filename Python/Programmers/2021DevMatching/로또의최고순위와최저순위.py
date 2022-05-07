def solution(lottos, win_nums):
    matched = list(m for m in lottos if m in win_nums)
    available = list(a for a in win_nums if a not in matched)
    if 1 < len(matched) < 6:
        x = 7 - len(matched)
    elif len(matched) == 6:
        return [1, 1]
    else:
        x = 6
    print(matched, available)
    if lottos.count(0) > len(available):
        y = len(matched) + len(available)
    else:
        y = len(matched) + lottos.count(0)
    if y > 1:
        y = 7 - y
    else:
        y = 6
    
    return [y, x]