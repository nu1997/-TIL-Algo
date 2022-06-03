from itertools import combinations as cb

N, M = map(int, input().split())
cards = list(map(int, input().split()))
# cards.sort(reverse=True)

card_list = list(cb(cards, 3))
maximum = 0
for card in card_list:
    if M >= sum(card) > maximum:
        maximum = sum(card)
print(maximum)