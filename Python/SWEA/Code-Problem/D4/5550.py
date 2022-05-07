T = int(input())
for tc in range(1, T+1):
    text = list(input())
    croak = ['c', 'r', 'o', 'a', 'k']
    temp = [[]] * 5
    # print(temp)
    print(text)
    # 0 1 2 3 4 ...
    for i in range(len(text)):
        for j in range(len(croak)):
            if text[i] == croak[j]:
                temp[j].append(i)
    print(temp)
    print(text)