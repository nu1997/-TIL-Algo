# T = int(input())
# for tc in range(1, T+1):
#     N = input()
#     l = len(N)
#     cnt = 0
#     word = []
#     for i in range(1, l+1):
#         for j in range(0, l):
#             if j+i <= l:
#                 # print(j, j+i, '-', N[j:j+i])
#                 word = N[j:j + i]
#                 if word == word[::-1]:
#                     cnt += 1
#                     print(word)
#     print('#%d' % tc, cnt)

T = int(input())
for tc in range(1, T+1):
    N = sorted(list(input()))
    l = len(N)
    cnt = 0
    for i in range(1, l+1):
        for j in range(l+1 - i):
            if j+i <= l:
                # print(j, j+i, '-', N[j:j+i])
                word = N[j:j + i]
                if word == word[::-1]:
                    cnt += 1
                    # print(word)
    print('#%d' % tc, cnt)
