T = int(input())

for t in range(1, T+1):
    N = int(input())
    card_number = input()
    counts = [0] * 10
    for n in range(len(card_number)):
        counts[int(card_number[n])] += 1
    max_num = 0
    max_idx = 0
    for i in range(len(counts)):
        if counts[i] >= max_num:
            max_num = counts[i]
            max_idx = i
    print('#%d %d %d' % (t, max_idx, max_num))