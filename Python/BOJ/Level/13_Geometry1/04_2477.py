N = int(input())

lst = []
for _ in range(6):
    dir, length = map(int, input().split())
    lst.append((dir,length))
print(lst)