#!/usr/bin/env python3

from random import choice
import random
import statistics


# Random Module
seq = ["heads", "tails"]
print(choice(seq))

nbr = random.randint(1, 100)
print(nbr)

cards = ["king", "queen", "Joker", "cupide", "traitor", "witch"]
random.shuffle(cards)
for card in cards:
    print(card)


# Statistics Module
nbrs = [21, 3435, -984, 547, 6291, 81, 3867, -873, -1891, 4314, 37, 95]
print(statistics.mean(nbrs))
