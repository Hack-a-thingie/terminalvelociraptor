import random
import defs
from player import *
"""This file contains the functionality of the Action cards, such as attack, grants etc."""
agencies = ["Grand Bullshit Foundation", "Schnobel Science Treasury", "Nippon Hikikomori Kyoukai"]

class Action(Card):
    """ Mother class for all action cards
    """
    def __init__(self, name, cost, description, effect):
        super(Action, self).__init__(name, cost, description)
        self.effect = effect

    def play(self, player):
        pass

    @property
    def successMessage(self):
        """
        :return: Message which can be displayed in case of success
        """
        curAg = random.randint(0, len(agencies)-1)
        return "Congratulations! You managed to hit a score with the %s funding agency and got lots of money!"\
        %(agencies[curAg])

    @property
    def failureMessage(self):
        """
        :return:  Message which can be displayed in case of failure
        """
        curAg = random.randint(0, len(agencies)-1)
        return "Alas! The %s funding agency decided you are lame and gave the money to someone else."\
        %(agencies[curAg])


class BigGrant(Action):
    """ Apply to big grant card. Costs a lot but brings in lots of BP"""
    def __init__(self):
        name = 'Apply for a Big Grant'
        cost = defs.Points(0, 15, 0, 0, 0, 0)
        effect = defs.Points(4, 0, 0, 0, 0, 0)
        self.bonusBS = 2
        description = "Get greedy! Apply for a big grant from a big funding agency.\n"\
        "Requires a lot of lies, connections and time, but your lab is getting rich indeed if successful.\n"\
        "Cost: %s.\nYou gain: %s and %d bonus budget slot%s"\
                      %(cost.__repr__(), effect.__repr__(), self.bonusBS, '' if self.bonusBS == 1 else 's')
        super(BigGrant, self).__init__(name, cost, description, effect)

    def isPlayable(self, player):
        """
        :param player: The player who is attempting to play the card
        :return: True if the card is ok to play and False otherwise
        """
        return True if player.points>=self.cost else False

    def play(self, player):
        """
        :param player: Player who is playing the card
        :return: True if success and False if failure
        """
        # TODO: Add trigger
        if self.isPlayable(player):
            player.points = player.points - self.cost
            player.points = player.points + self.effect
            player.bs += self.bonusBS
            return True
        else:
            return False




def boom(self, player, dmg):
    player.points.APB = player.points.APB - dmg
    if player.points.APB < 0:
        player.points.APB = 0


Action.play = classmethod(boom)

def my_action():
    print 12

my_action_card = Action("Adi's wrath", defs.Points(0, 0, 0, 0, 0, 0), "", my_action)
#my_action_card.play(1)
player1 = Player("Irina")
player1.points.APB = 12
print player1.points.APB
grant = BigGrant()
print grant.description
resources = defs.Points(0,13,0,0,0, 0)
player1.points = resources
print resources
print grant.cost
print resources >=grant.cost
if grant.play(player1):
    print grant.successMessage
else:
    print grant.failureMessage