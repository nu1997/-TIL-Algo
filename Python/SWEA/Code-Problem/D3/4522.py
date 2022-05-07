# 4522. 세상의 모든 팰린드롬

# T = int(input())
# for tc in range(1, T+1):
#     word = input()
#     is_palin = ''
#     idx = []
#     for i in range(len(word)):
#         if word[i] == '?':
#             idx.append(len(word) - i - 1)
#     for i in range(len(word)):
#         if i in idx:
#             pass
#         else:
#             is_palin += word[i]
#     # print(is_palin)
#     if is_palin == is_palin[::-1]:
#         res = 'Exist'
#     else:
#         res = 'Not exist'
#     print('#%d' % tc, res)

def ispalin(s):
    for i in range(len(s) // 2):
        if (s[i] == s[len(s) - 1 - i]) or s[i] == '*' or s[len(s) - 1 - i] == '*':
            continue
        else:
            return 'Not exist'
    return 'Exist'


T = int(input())
for t in range(1, T + 1):
    S = input()
    print("#%d %s" % (t, ispalin(S)))