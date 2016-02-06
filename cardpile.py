
from defs import *


class CardPile (object):
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_first_card(self):
        return self.cards.pop(0)

    def remove_card(self, card_to_remove):
        if card_to_remove in self.cards:
            self.cards.remove(card_to_remove)

    def shuffle(self):
        random.shuffle(self.cards)

    def show(self):
        for card in self.cards:
            print card.name

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__