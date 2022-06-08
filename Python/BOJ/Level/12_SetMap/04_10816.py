import sys

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))

card_dict = dict()
for card in cards:
    try:
        card_dict[card] += 1
    except:
        card_dict[card] = 1

M = int(input())
check = list(map(int, sys.stdin.readline().split()))

ans = []
for c in check:
    try:
        ans.append(card_dict[c])
    except:
        ans.append(0)

print(*ans)



