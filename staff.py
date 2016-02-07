#!/usr/local/bin/python
# coding: latin-1

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
        self.category = random.choice(["PhD", "Udg", "MSc", "Doc", "Tch", "SSc", "Vis", "R.A"])
        self.face = random.choice(["@", "Ô ", "Ō", "Ö", "Ò", "Ó", "Ø", "Õ", "█", "ð", "©", "®"])
        self.hat = random.choice(["!", "? ", "$", ""])




    def __repr__(self):
        abilities = ""
        abilities += "\033[1;34;48mP\033[0m" * self.abilities.APP
        abilities += "\033[1;31;48mC\033[0m" * self.abilities.APC
        abilities += "\033[1;32;48mB\033[0m" * self.abilities.APB
        abilities += "\033[1;39;48mM\033[0m" * self.abilities.APM
        return "\n  %s  \n  %s  \n╔═══╗\n║%s║\n%s" % (self.hat, self.face, self.category, abilities)

    def play(self, player):
        self.played = True
        player.remove_from_hand(self)
        player.unit.add_card(self)

    def buffs(self, buff):
        self.abilities += buff

