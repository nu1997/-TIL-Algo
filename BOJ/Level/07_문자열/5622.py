ans = 0
for i in input():
    if ord(i) < 83:
        ans += (ord(i) - 65) // 3 + 3
    elif ord(i) == 83:
        ans += 8
    elif 83 < ord(i) < 87:
        ans += 9
    else:
        ans += 10
print(ans)