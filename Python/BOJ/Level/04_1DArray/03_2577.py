res = 1
for _ in range(3):
    res *= int(input())
cnt = [0] * 10
for i in str(res):
    cnt[int(i)] += 1
for i in range(10):
    print(cnt[i])