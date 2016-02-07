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

    def __add__(self, other):
        return Points(self.BP + other.BP, \
                      self.APG + other.APG, \
                      self.APP + other.APP, \
                      self.APC + other.APC, \
                      self.APM + other.APM, \
                      self.APB + other.APB)

    @property
    def toString(self):
        """ Convert the structure into an intelligible string. """
        string = "BP: %d, APG: %d, APP: %d, "\
                 "APC: %d, APM: %d, APB: %d" \
                 %(self.BP, self.APG, self.APP, self.APC, self.APM, self.APB)
        return string


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





