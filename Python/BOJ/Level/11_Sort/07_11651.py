def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser, equal, greater = [], [], []
    for pair in arr:
        if pair[1] < pivot[1]:
            lesser.append(pair)
        elif pair[1] > pivot[1]:
            greater.append(pair)
        else:
            if pair[0] < pivot[0]:
                lesser.append(pair)
            elif pair[0] > pivot[0]:
                greater.append(pair)
            else:
                equal.append(pair)
    return quicksort(lesser) + equal + quicksort(greater)

N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

ans = quicksort(lst)
for pair in ans:
    print(*pair)