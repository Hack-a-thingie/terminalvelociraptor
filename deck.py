
from cardpile import *
from staff import *


class Deck(CardPile):
    def __init__(self, discardpile):
        super(Deck, self).__init__()
        self.discardpile = discardpile

    def get_first_card(self):
        if self.is_empty():
            self.discardpile.shuffle()
            while not self.discardpile.is_empty():
                self.add_card(self.discardpile.cards.pop(0))

        card_to_give = self.cards.pop(0)

        return card_to_give

graveyard = CardPile()
gamedeck = Deck(graveyard)



