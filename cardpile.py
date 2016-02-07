
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
            print card.name

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def is_empty(self):
        return self.cards == []

    def shuffle(self):
        random.shuffle(self.cards)



class Deck(CardPile):
    def __init__(self, discardpile):
        super(Deck, self).__init__()
        self.discardpile = discardpile

    def get_first_card(self):
        if self.is_empty():
            print "HOW DID THIS HAPPEN?"
        else:
            card_to_give = self.cards.pop(0)

        if self.is_empty():
            self.discardpile.shuffle()
            while not self.discardpile.is_empty():
                self.add_card(self.discardpile.cards.pop(0))

        return card_to_give
