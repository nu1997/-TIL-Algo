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
def solution(v):
    answer = []
    x = set()
    y = set()
    for p in v:
        x.add(p[0])
        y.add(p[1])
    x = list(x)
    y = list(y)
    for i in range(2):
        for j in range(2):
            if [x[i],y[j]] not in v:
                return [x[i], y[j]]
'''

'''
# XOR 연산 - 왜인지 메모리, 시간은 똑같다. 
x = pair[0][0] ^ pair[1][0] ^ pair[2][0]
y = pair[0][1] ^ pair[1][1] ^ pair[2][1]

print(x, y)
'''