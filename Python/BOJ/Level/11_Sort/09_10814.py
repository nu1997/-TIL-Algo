def quicksort(arr):
    if len(arr) <= 1:
        return arr
    lesser, equal, greater = [], [], []
    pivot = arr[len(arr) // 2]
    for pair in arr:
        if pair[0] < pivot[0]:
            lesser.append(pair)
        elif pair[0] > pivot[0]:
            greater.append(pair)
        else:
            if pair[2] < pivot[2]:
                lesser.append(pair)
            elif pair[2] > pivot[2]:
                greater.append(pair)
            else:
                equal.append(pair)
    return quicksort(lesser) + equal + quicksort(greater)

N = int(input())
member = []
for i in range(N):
    age, name = input().split()
    member.append((int(age), name, i))
ans = quicksort(member)
for pair in ans:
    print(pair[0], pair[1])

''' quicksort가 오래걸릴 때, 그리고 인덱스값 추가 없이
https://velog.io/@cookncoding/알고리즘-개념-Stable-Sort-Inplace

#stable 정렬을 해야 한다. >> mergesort
import sys

N = int(sys.stdin.readline())
names= []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    names.append([age,name])


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) //2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

   
    l ,h, k = 0, 0, 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l][0] <= high_arr[h][0]:
            arr[k] = (low_arr[l])
            l += 1

        else:
            arr[k] = (high_arr[h])
            h += 1
        k += 1
    if l == len(low_arr):
        while h < len(high_arr):
            arr[k] = high_arr[h]
            h += 1
            k +=1
    elif h == len(high_arr):
        while l < len(low_arr):
            arr[k] = low_arr[l]
            l += 1
            k += 1
    return arr

merge_sort(names)

for i in names:
    print(i[0], i[1])
'''