# 듣보잡

''' ver 1
N, M = map(int, input().split())
name, ans = [], []
for _ in range(N):
    name.append(input())
for _ in range(M):
    x = input()
    if x in name:
        ans.append(x)

print(len(ans))
for x in sorted(ans):
    print(x)
'''

''' ver 2
import sys

N, M = map(int, sys.stdin.readline().split())
name, ans = [], []
for _ in range(N):
    name.append(sys.stdin.readline().rstrip())
for _ in range(M):
    x = input()
    if x in name:
        ans.append(x)

print(len(ans))
for x in sorted(ans):
    print(x)
'''
import sys

N, M = map(int, sys.stdin.readline().split())
name, ans = dict(), set()
for _ in range(N):
    name[sys.stdin.readline().rstrip()] = 1
for _ in range(M):
    x = sys.stdin.readline().rstrip()
    try:
        if name[x]:
            ans.add(x)
    except:
        pass

print(len(ans))
for x in sorted(ans):
    print(x)
