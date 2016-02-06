"""
definitions
"""

import random

class Points(object):
    """Contains all information regarding in-game points - action points and budget points."""
    def __init__(self, BP, APG, APP, APC, APM, APB):
        self.BP = BP    # Budget Points
        self.APG = APG  # Action Points: General
        self.APP = APP  # Action Points: Physics
        self.APC = APC  # Action Points: Chemistry
        self.APM = APM  # Action Points: Mathematics
        self.APB = APB  # Action Points: Biology


class Card(object):
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

    def play(self, player):
        pass


class Reaction(Card):
    def __init__(self, name, cost, description, trigger, effect):
        super(Reaction, self).__init__(name, cost, description)
        self.trigger = trigger
        self.effect = effect

    def play(self, player):
        # ...
        pass


class Action(Card):
    def __init__(self, name, cost, description, effect):
        super(Action, self).__init__(name, cost, description)
        self.effect = effect

    def play(self, player):
        self.effect()

"""
def my_action():
    print 12

my_action_card = Action("Adi's wrath", Points(0, 0, 0, 0, 0, 0), "", my_action)
my_action_card.play(1)
"""


class CardPile (object):
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_first_card(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)


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

    def increase_bs_with_max(self, max):
        if self.bs < max:
            self.bs += 1

    def set_bp_to_bs(self):
        self.points.BP = self.bs

    def get_staff_cost(self):
        staff_cost = 0
        for staff in self.unit.cards:
            staff_cost += staff.cost
        return staff_cost

    def get_staff_bp(self):
        return self.Points(0)

    def update_staff_abilities(self):
        for staff in self.unit.cards:
            self.Points += staff.abilities
