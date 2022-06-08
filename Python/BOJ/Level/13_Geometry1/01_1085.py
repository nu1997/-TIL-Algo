# 직사각형에서 탈출

x, y, w, h = map(int, input().split())
# t, b, l, r = h - y, y, x, w -x
t, r = h - y, w - x
print(min(t, r, x, y))
