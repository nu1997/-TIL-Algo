pair = []

for _ in range(3):
    pair.append(tuple(map(int, input().split())))

x, y = [], []
for coor in pair:
    if coor[0] in x:
        x.remove(coor[0])
    else:
        x.append(coor[0])
    if coor[1] in y:
        y.remove(coor[1])
    else:
        y.append(coor[1])
print(*x, *y)
