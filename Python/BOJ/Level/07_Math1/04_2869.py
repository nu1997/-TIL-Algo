# 달팽이는 올라가고 싶다
A, B, V = map(int, input().split())
ans = (V-B) // (A-B)
if (V-B) % (A-B):
    ans += 1
print(ans)
# day = 0
# height = 0
# while True:
#     if height >= V:
#         print(day)
#         break
#     height += A
#     if height < V:
#         height -= B
#     day += 1
