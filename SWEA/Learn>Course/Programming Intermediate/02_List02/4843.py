
def special_sort(array, n):
    for i in range(n):
        if i % 2 == 0:
            maxIdx = i
            for j in range(i+1, n):
                if array[maxIdx] < array[j]:
                    maxIdx = j
            array[i], array[maxIdx] = array[maxIdx], array[i]
        else:
            minIdx = i
            for j in range(i+1, n):
                if array[minIdx] > array[j]:
                    minIdx = j
            array[i], array[minIdx] = array[minIdx], array[i]
    return array[:10] # 10개까지만 출력

T = int(input())
for t in range(1, T+1):
    N = int(input()) # 정수의 개수
    num_list = list(map(int, input().split()))

    print('#%d' % t, *(special_sort(num_list, N)))
