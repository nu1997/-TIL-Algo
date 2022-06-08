def quicksort(arr):
    if len(arr) <= 1:
        return arr
    lesser, equal, greater = [], [], []
    pivot = arr[len(arr) // 2]
    for word in arr:
        if len(word) < len(pivot):
            lesser.append(word)
        elif len(word) > len(pivot):
            greater.append(word)
        else:
            equal.append(word)
    return quicksort(lesser) + sorted(equal) + quicksort(greater)

N = int(input())
S = set()
for _ in range(N):
    S.add(input())
ans = quicksort(list(S))
for word in ans:
    print(word)