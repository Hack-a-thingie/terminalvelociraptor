from defs import *


def __init__(self, name, cost, description, abilities):
    super(Staff, self).__init__(name, cost, description)
    self.original_abilities = abilities
    self.abilities = abilities
    self.played = False


def play(self, player):
    self.played = True
    player.removefromhand(self)
    player.addmember(self)
    player.cost(self.cost)
    update(self, player)


def update(self, player):
    player.abilities(self.abilities)


def buffs(self, buff):
    self.abilities += buff





# staff_card_Bob = Staff(name, cost, description, abilities)

Mark = Staff("Mark, the intern", Points(1, 0, 0, 0, 0, 0), "Generic Physics undergrad", Points(0, 0, 1, 0, 0, 0))
Bob = Staff("Bob", Points(1, 0, 0, 0, 0, 0), "Generic Maths undergrad", Points(0, 0, 0, 0, 0, 1))
