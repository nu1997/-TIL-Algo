def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    else:
        while d:
            d.remove(max(d))
            return solution(d, budget)