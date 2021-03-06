
from cardpile import *
from deck import *

players = []

def get_other_player(player):
    for other_player in players:
        if not other_player is player:
            return other_player


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
            # TODO: I think it does not make sense to have this here (see deck.get_first_card())
            print("Could not draw a card")
            return False

    def remove_from_hand(self, card_to_remove):
        self.hand.remove_card(card_to_remove)

    def increase_bs_with_max(self, max):
        if self.bs < max:
            self.bs += 1

    def set_points_to_staff_and_bs(self):
        self.points = Points(0,0,0,0,0,0)
        self.points += self.get_staff_abilities()
        self.points.BP += self.bs

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
        graveyard.add_card(self.unit.cards.pop(0))

    def discard_card(self):
        graveyard.add_card(self.hand.cards.pop(0))