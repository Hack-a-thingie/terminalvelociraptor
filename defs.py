"""
Base Card Class
"""

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


class Staff(Card):
    def __init__(self, name, cost, description, abilities):
        super(Staff, self).__init__(name, cost, description)
        self.original_abilities = abilities
        self.abilities = abilities
        self.played = False

    def play(self, player):
        self.played = True
        player.unit.append(self)
        # ...


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


def my_action():
    print 12

my_action_card = Action("Adi's wrath", Points(0, 0, 0, 0, 0, 0), "", my_action)
my_action_card.play(1)

