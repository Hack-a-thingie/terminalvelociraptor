
from cardpile import *



class Player (object):
    def __init__(self, name):
        self.name = name
        self.hand = CardPile()
        self.unit = CardPile()
        self.reactions = CardPile()
        self.points = Points(0, 0, 0, 0, 0, 0)
        self.impact = 0
        self.bs = 0

    def draw_card(self, deck):
        drawn_card = deck.get_first_card()
        if drawn_card != 0:
            self.hand.add_card(drawn_card)
            return True
        else:
            print "Could not draw a card"
            return False

    def remove_from_hand(self, card_to_remove):
        self.hand.remove_card(card_to_remove)

    def increase_bs_with_max(self, max):
        if self.bs < max:
            self.bs += 1

    def set_bp_to_bs(self):
        self.points.BP = self.bs

    def get_staff_cost(self):
        staff_cost = 0
        for staff in self.unit.cards:
            staff_cost += staff.cost.BP
        return staff_cost

    def get_staff_bp(self):
        return self.Points(0)

    def get_staff_abilities(self):
        total = Points(0,0,0,0,0,0)
        for staff in self.unit.cards:
            total += staff.abilities
        return total

    def fire_someone(self):
        self.unit.cards.pop(0)