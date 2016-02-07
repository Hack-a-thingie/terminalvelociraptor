#import random
import math
import defs
from player import *
from reactions import *
"""This file contains the functionality of the Action cards, such as attack, grants etc."""
agencies = ["Grand Bullshit Foundation", "Schnobel Science Treasury", "Nippon Hikikomori Kyoukai", "Beggars-are-choosers Backwater Investment Co", "Uncle Sam Science Support", "Abu Douchebag Memorial Fund"]
people = ["loyal dog belonging to someone", "janitor", "night guard", "cook", "accountant", "someone's relative", "undergraduate student", "master student", "PhD student", "postdoc", "professor", "manager", "dean", "Nobel prize laureate"]
class Action(Card):
    """ Mother class for all action cards
    """
    def __init__(self, name, cost, description, effect):
        super(Action, self).__init__(name, cost, description)
        self.effect = effect

    def play(self, player):
        super(Action, self).play(player)

    @property
    def successMessage(self):
        """
        :return: Message which can be displayed in case of success
        """
        return "Congratulation! Your action was successful"

    @property
    def failureMessage(self):
        """
        :return:  Message which can be displayed in case of failure
        """
        return "Booo you failed to execute the action."


class BigGrant(Action):
    """ Apply to big grant card. Costs a lot but brings in lots of BP"""
    def __init__(self):
        name = 'Apply for a Big Grant'
        cost = defs.Points(0, 15, 0, 0, 0, 0)
        effect = defs.Points(4, 0, 0, 0, 0, 0)
        self.bonusBS = 2
        self.bonusIF = 6
        description = "Get greedy! Apply for a big grant from a big funding agency.\n"\
        "Requires a lot of lies, connections and time, but your lab is getting rich indeed if successful.\n"\
        "Cost: %s.\nYou gain: %s, %d bonus budget slot%s and %d additional impact factor"\
                      %(cost.__repr__(), effect.__repr__(), self.bonusBS, \
                        '' if self.bonusBS == 1 else 's', self.bonusIF)
        super(BigGrant, self).__init__(name, cost, description, effect)

    def play(self, player):
        """
        :param player: Player who is playing the card
        :return: True if success and False if failure
        """
        super(BigGrant, self).play(player)
        # TODO: Test trigger
        if self.is_playable(player):
            # player.remove_from_hand(self)
            # need to discard to graveyard - done in master function
            # player.points = player.points - self.cost
            player.points = player.points + self.effect
            player.bs += self.bonusBS
            player.impact += self.bonusIF
            trigger_happened(player, trigger_dict["TRIGGER_GRANT"])
            return True
        else:
            return False
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

class MediumGrant(Action):
    """ Apply for a medium grant. Costs quite a bit of time, but results in decent budget increase
    """
    def __init__(self):
        name = 'Apply for a Medium Grant'
        cost = defs.Points(0, 10, 0, 0, 0, 0)
        effect = defs.Points(2, 0, 0, 0, 0, 0)
        self.bonusBS = 2
        self.bonusIF = 3
        description = "Time to get stuffed! Apply for a medium grant from a funding agency.\n"\
        "Requires some lies and time, but your lab gets well stocked if successful.\n"\
        "Cost: %s.\nYou gain: %s, %d bonus budget slot%s and %d additional impact factor"\
                      %(cost.__repr__(), effect.__repr__(), self.bonusBS, \
                        '' if self.bonusBS == 1 else 's', self.bonusIF)
        super(MediumGrant, self).__init__(name, cost, description, effect)

    # def is_playable(self, player):
    #     """
    #     :param player: The player who is attempting to play the card
    #     :return: True if the card is ok to play and False otherwise
    #     """
    #     return True if player.points>=self.cost else False

    def play(self, player):
        """
        :param player: Player who is playing the card
        :return: True if success and False if failure
        """
        super(MediumGrant, self).play(player)
        # TODO: Test trigger
        if self.is_playable(player):
            # player.points = player.points - self.cost
            player.points = player.points + self.effect
            player.bs += self.bonusBS
            player.impact += self.bonusIF
            trigger_happened(player, trigger_dict["TRIGGER_GRANT"])
            return True
        else:
            return False

    @property
    def successMessage(self):
        """
        :return: Message which can be displayed in case of success
        """
        curAg = random.randint(0, len(agencies)-1)
        return "Congratulations! You managed to convince the %s funding agency to give you a considerable sum of money!"\
        %(agencies[curAg])

    @property
    def failureMessage(self):
        """
        :return:  Message which can be displayed in case of failure
        """
        curAg = random.randint(0, len(agencies)-1)
        return "Alas! The %s funding agency decided you are lame and gave the money to someone else."\
        %(agencies[curAg])

class SmallGrant(Action):
    """ Apply for a small grant. Costs some time and results in a humble budget increase
    """
    def __init__(self):
        name = 'Apply for a Small Grant'
        cost = defs.Points(0, 3, 0, 0, 0, 0)
        effect = defs.Points(1, 0, 0, 0, 0, 0)
        self.bonusIF = 1
        description = "Time to beg for some pocket cash! Apply for a small grant"\
                    "by asking for donations at the local science fair.\n"\
        "Requires a bit of time, but your lab gets some change from the grandma.\n"\
        "Cost: %s.\nYou gain: %s and %d additional impact factor"\
                      %(cost.__repr__(), effect.__repr__(), self.bonusIF)
        super(SmallGrant, self).__init__(name, cost, description, effect)

    # def is_playable(self, player):
    #     """
    #     :param player: The player who is attempting to play the card
    #     :return: True if the card is ok to play and False otherwise
    #     """
    #     return True if player.points>=self.cost else False

    def play(self, player):
        """
        :param player: Player who is playing the card
        :return: True if success and False if failure
        """
        super(SmallGrant, self).play(player)
        # TODO: Test trigger
        if self.is_playable(player):
            # player.points = player.points - self.cost
            player.points = player.points + self.effect
            player.impact += self.bonusIF
            trigger_happened(player, trigger_dict["TRIGGER_GRANT"])
            return True
        else:
            return False

    @property
    def successMessage(self):
        """
        :return: Message which can be displayed in case of success
        """
        curAg = random.randint(0, len(agencies)-1)
        return "Congratulations! You managed to look miserable enough so a grandma from %s funding agency gave you some coins!"\
        %(agencies[curAg])

    @property
    def failureMessage(self):
        """
        :return:  Message which can be displayed in case of failure
        """
        return "Alas! Your alms box stays empty."

class Workshop(Action):
    """ Attend a workshop
    """
    def __init__(self):
        name = "Attend a workshop"
        cost = defs.Points(1, 2, 0, 0, 0, 0)
        effect = defs.Points(0, 0, 0, 0, 0, 0)
        self.bonusIF = 1
        description = "Attend a workshop. Doesn't cost much, but don't expect getting much out of it either.\n"\
        "Cost: %s. You gain %d bonus impact factor."%(cost.__repr__(), self.bonusIF)
        super(Workshop, self).__init__(name, cost, description, effect)

    @property
    def successMessage(self):
        """
        :return: Message which can be displayed in case of success
        """
        curP = random.randint(0, math.floor(len(people)/2))
        return "Congratulations! You met a %s from one of the top universities!\n"\
                "Now people know you there and your impact factor has slightly increased."%(people[curP])

    @property
    def failureMessage(self):
        """
        :return:  Message which can be displayed in case of failure
        """
        return "Unfortunately, you didn't meet anyone important."

    # def is_playable(self, player):
    #     """
    #     :param player: The player who is attempting to play the card
    #     :return: True if the card is ok to play and False otherwise
    #     """
    #     return True if player.points>=self.cost else False

    def play(self, player):
        """
        :param player: Player who is playing the card
        :return: True if success and False if failure
        """
        super(Workshop, self).play(player)
        # TODO: Test trigger
        if self.is_playable(player):
            # player.points = player.points - self.cost
            player.points = player.points + self.effect
            player.impact += self.bonusIF
            trigger_happened(player, trigger_dict["TRIGGER_CONFERENCE"])
            return True
        else:
            return False
