T = int(input())
for tc in range(1, T+1):
    word = input()
    if word[0] != '*' and word[-1] != '*':
        replaced = word.replace('*', '')
        if replaced == replaced[::-1]:
            res = 'Exist'
        else:
            res = 'Not exist'
    else:
        res = 'Exist'
    print('#%d' % tc, res)
