cnt = set()
for _ in range(10):
    n = int(input())
    cnt.add(n % 42)
print(len(cnt))