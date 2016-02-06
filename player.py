
from cardpile import *


class Player (object):
    def __init__(self):
        self.hand = CardPile()
        self.unit = CardPile()
        self.reactions = CardPile()
        self.points = Points(0, 0, 0, 0, 0, 0)
        self.impact = 0
        self.bs = 0

    def draw_card(self, deck):
        self.hand.add_card(deck.get_first_card())

    def remove_from_hand(self, deck):
        pass

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

    def update_staff_abilities(self):
        for staff in self.unit.cards:
            self.Points += staff.abilities