"""
whatever adi tried to do with the staff cards
"""


from cardpile import *

class Staff(Card):
    def __init__(self, name, cost, description, abilities):
        super(Staff, self).__init__(name, cost, description)
        self.original_abilities = abilities
        self.abilities = abilities
        self.played = False

    def play(self, player):
        self.played = True
        player.remove_from_hand(self)
        player.unit.add_card(self)

    def buffs(self, buff):
        self.abilities += buff

