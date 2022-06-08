pair = []

for _ in range(3):
    pair.append(tuple(map(int, input().split())))

# 그리디 - 넣었다 뺏다
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

'''
# XOR 연산 - 왜인지 메모리, 시간은 똑같다. 
x = pair[0][0] ^ pair[1][0] ^ pair[2][0]
y = pair[0][1] ^ pair[1][1] ^ pair[2][1]

print(x, y)
'''