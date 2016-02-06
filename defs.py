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

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__


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





