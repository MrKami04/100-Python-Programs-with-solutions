# program that to shuffle deck of cards
print("😍 ------------------------- 😍")

import random, itertools
deck_cards = list(itertools.product(range(1, 14), ["spade", "club", "hearts"," diamond"]))

random.shuffle(deck_cards)
print(deck_cards)
for i in range(5):
    print(deck_cards[i][0],"of" , deck_cards[i][1])


