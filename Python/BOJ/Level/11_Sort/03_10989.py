# 카운팅 정렬 

''' 메모리 초과
N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))
limit = max(nums) + 1

count = [0] * limit
# check = [0] * limit
ans = [0] * N

for num in nums:
    # check[num] += 1
    while num < limit:
        count[num] += 1
        num += 1

for i in range(N-1, -1, -1): #987654321
    count[nums[i]] -= 1
    ans[count[nums[i]]] = nums[i]

for num in ans:
    print(num)
'''
#  https://www.acmicpc.net/board/view/26132

# 1. 모든 입력을 배열에 저장하면 당연히 메모리 초과입니다. 문제의 메모리 제한은 겨우 8MB입니다. 아무리 작은 자료형으로 저장한다고 해도 short형 (2바이트) 천만 개면 약 20MB로 역시 메모리 초과입니다. 입력을 전부 저장하지 않고 푸는 방법을 생각해 보세요. 힌트는 입력되는 정수의 범위에 있습니다.
# 2. (C++) endl 쓰지 말고 '\n' 쓰세요. endl은 버퍼를 flush하기 때문에 매우, 매우, 매우 느립니다. 이건 이 문제 뿐만이 아니라 앞으로 푸실 모든 문제에 대해 공통입니다.
# 3. int a[10000]; 의 원소는 9999까지입니다.
# 4. 느린 입출력을 써도 시간 초과가 될 수 있습니다. https://www.acmicpc.net/problem/15552 에서 내가 충분히 빠른 입출력을 쓰고 있는지 확인해 보세요.
# 5. Pypy를 쓸 경우 print가 아니라 sys.stdout.write를 해야 메모리 초과를 받지 않습니다.

import sys

# N = int(input())
N = int(sys.stdin.readline().rstrip())
count = [0] * 10001
for _ in range(N):
    count[int(sys.stdin.readline().rstrip())] += 1

for idx, val in enumerate(count):
    if val:
        for _ in range(val):
            print(idx)