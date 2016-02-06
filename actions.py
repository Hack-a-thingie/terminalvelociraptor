import defs

"""This file contains the functionality of the Action cards, such as attack, grants etc."""

def boom(self, player, dmg):
    player.points.APB = player.points.APB - dmg
    if player.points.APB < 0:
        player.points.APB = 0


defs.Action.play = classmethod(boom)

def my_action():
    print 12

my_action_card = defs.Action("Adi's wrath", defs.Points(0, 0, 0, 0, 0, 0), "", my_action)
#my_action_card.play(1)
player1 = defs.Player()
player1.points.APB = 12
my_action_card.play(player1, 10)
print player1.points.APB