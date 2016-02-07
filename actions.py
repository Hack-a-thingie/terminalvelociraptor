import defs
from player import *
"""This file contains the functionality of the Action cards, such as attack, grants etc."""
class BigGrant(defs.Action):
    """ Apply to big grant card. Costs a lot but brings in lots of BP"""
    def __init__(self):
        name = 'Apply for a Big Grant'
        cost = defs.Points(0, 15, 0, 0, 0, 0)
        effect = defs.Points(4, 0, 0, 0, 0, 0)
        bonusBS = 2
        description = "Get greedy! Apply for a big grant from a big funding agency.\n"\
        "Requires a lot of lies, connections and time, but your lab is getting rich indeed if successful.\n"\
        "Cost: %s.\nYou gain: %s and %d bonus budget slot%s"\
                      %(cost.toString, effect.toString, bonusBS, '' if bonusBS == 1 else 's')
        super(BigGrant, self).__init__(name, cost, description, effect)

def boom(self, player, dmg):
    player.points.APB = player.points.APB - dmg
    if player.points.APB < 0:
        player.points.APB = 0


defs.Action.play = classmethod(boom)

def my_action():
    print 12

my_action_card = defs.Action("Adi's wrath", defs.Points(0, 0, 0, 0, 0, 0), "", my_action)
#my_action_card.play(1)
player1 = Player("Irina")
player1.points.APB = 12
my_action_card.play(player1, 10)
print player1.points.APB
grant = BigGrant()
print grant.description