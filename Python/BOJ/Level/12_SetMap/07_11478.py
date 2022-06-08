''' ver 1 - 문제를 잘못 해석함
# 비트연산으로 부분집합 구하기
l = len(S)
for i in range(1, 1<<l):
    temp = ''
    for j in range(l):
        if i & (1<<j):
            temp += S[j]
    lst.append(temp)
'''

''' ver2 통과했지만 오래걸림 - 리스트 사용
import sys

S = list(sys.stdin.readline().rstrip())
l = len(S)

ans = set()
for i in range(l+1):
    for j in range(i+1, l+1):
        ans.add(''.join(S[i:j]))
print(len(ans))
'''

# ver 3 통과, 빠름 - 문자열 사용

import sys

S = sys.stdin.readline().rstrip()
l = len(S)
ans = set()
for i in range(l):
    for j in range(i+1, l+1):
        ans.add(S[i:j])
print(len(ans))