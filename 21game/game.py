from bean import Poker

p = Poker()
p.r_select()
for card in p.cards:
    print("{0}  {1}".format(card.color, card.name))
