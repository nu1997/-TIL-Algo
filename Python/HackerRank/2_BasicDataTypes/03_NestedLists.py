def solution(arr, flag):
    ans = []
    for el in arr:
        if el[1] == flag:
            ans.append(el[0])
    ans.sort()
    for el in ans:
        print(el)
    return
        


if __name__ == '__main__':
    arr = []
    score_set = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_set.add(score)
        arr.append([name, score])
    score_list = list(score_set)
    score_list.sort()
    flag = score_list[1]
    solution(arr, flag)