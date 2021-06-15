# def f(n):
#     temp = 0
#     for i in range(len(n)):
#         temp += int(n[i])
#     if temp > 9:
#         return f(str(temp))
#     return str(temp)
#
# ans = []
# T = int(input())
# for _ in range(1, T+1):
#     N = input()
#     ans.append(f(N))
#
# for tc, a in enumerate(ans, start=1):
#     print('#%d %s' % (tc, a))

def f(n):
    temp = sum(n)
    if temp > 9:
        return f(list(map(int, str(temp))))
    return temp

ans = []
T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input()))
    ans.append(f(N))
for tc, a in enumerate(ans, start=1):
    print('#%d %s' % (tc, a))

# T = int(input())
# for tc in range(1, T+1):
#     N = input()
#     while len(N) > 1:
#         temp = 0
#         for num in N:
#             temp += int(num)
#         N = str(temp)
#     print('#%d %s' % (tc, N))