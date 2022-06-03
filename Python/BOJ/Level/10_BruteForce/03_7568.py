N = int(input())

lst = []
for i in range(N):
    lst.append(input().split())

ans = []
for i in range(N):
    grade = 1
    for j in range(N):
        if int(lst[i][0]) < int(lst[j][0]) and int(lst[i][1]) < int(lst[j][1]):
            grade += 1
    ans.append(grade)
print(*ans)