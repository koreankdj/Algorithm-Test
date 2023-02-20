import sys
n = int(input())

cards = []
for i in range(n):
    cards.append(i+1)

while len(cards) > 1:
    del [cards[0]]
    cards.insert(len(cards),cards[0])
    del [cards[0]]
else:
    for card in cards:
        print(card)
