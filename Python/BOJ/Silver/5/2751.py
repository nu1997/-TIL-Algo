# 수 정렬하기 2
'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 
수는 중복되지 않는다.

시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있습니다. 
예를 들면 병합 정렬, 힙 정렬 등이 있지만, 
어려운 알고리즘이므로 지금은 언어에 내장된 정렬 함수를 쓰는 것을 추천드립니다.
'''
import sys

# 힙 정렬 heap sort
# 퀵 정렬 quick sort
# 카운트 정렬 count sort
# 내장함수 sort()

# 병합 정렬 merge sort
def merge_sort1(arr):
    def merge(left, right):
        result = []

        # left, right 원소가 남아있는 경우
        while len(left) and len(right):
            # left, right 두 서브 리스트의 첫 원소들을 비교하여 작은 것부터 result에 추가
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        if len(left) > 0: # 왼쪽 리스트에 원소가 남아있는 경우
            result.extend(left)
        
        if len(right) > 0: # 오른쪽 리스트에 원소가 남아있는 경우
            result.extend(right)
        return result

    def sort(m):
        if len(m) <= 1:
            return m

        # divide
        mid = len(m) // 2
        left = m[:mid]
        right = m[mid:]
        
        # recursion
        left = merge_sort(left)
        right = merge_sort(right)

        # conquer
        return merge(left, right)
    return sort(arr)

# 병합 정렬 merge sort - optimized
def merge_sort2(arr):
    def sort(left, right):
        print('sort function:', left, right)
        if right - left < 2:
            print('right - left < 2: ', left, right)
            return
        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        print('merge function: ', left, mid, right)
        temp = []
        l, h = left, mid

        while l < mid and h < right:
            if arr[l] < arr[h]:
                print(arr[l], '<', arr[h])
                temp.append(arr[l])
                l += 1
            else:
                print(arr[l], '>=', arr[h])
                temp.append(arr[h])
                h += 1

        while l < mid:
            print(l, '<', mid)
            temp.append(arr[l])
            l += 1
        while h < right:
            print(h, '<', right)
            temp.append(arr[h])
            h += 1

        for i in range(left, right):
            arr[i] = temp[i - left]
            print(arr)

    return sort(0, len(arr))

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
# nums.sort()
print(nums)
merge_sort2(nums)
# print(*nums, sep='\n')