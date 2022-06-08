import sys

N, M = map(int, input().split())

check = set()
for _ in range(N):
    check.add(sys.stdin.readline().rstrip())

words = []
for _ in range(M):
    words.append(sys.stdin.readline().rstrip())

cnt = 0
for word in words:
    if word in check:
        cnt += 1

print(cnt)