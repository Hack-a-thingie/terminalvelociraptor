import random
from defs import *


class CardPile (object):
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card_to_remove):
        if card_to_remove in self.cards:
            self.cards.remove(card_to_remove)

    def show(self):
        for card in self.cards:
            print(card.name)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def is_empty(self):
        return self.cards == []

    def shuffle(self):
        random.shuffle(self.cards)

    def select_random_card(self):
        """
        :return: A random card from the pile
        """
        num = random.randint(0, len(self.cards)-1)
        return self.cards[num]
