import random


class Card():
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Poker():
    cards = []

    def __init__(self):
        for name in ["红桃", "黑桃", "方块", "梅花"]:
            for color in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                self.cards.append(Card(name, color))

    def r_select(self):
        random.shuffle(self.cards)
