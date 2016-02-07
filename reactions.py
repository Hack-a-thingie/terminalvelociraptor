"""This file contains the functionality of the Reaction cards"""

from defs import *
from player import *
"""
TRIGGERS ARE:
    - Publishing a paper
    - Getting a grant
    - Going to a conference
    - Hiring someone
"""
"""
def setup_triggers():
    global _TRIGGER_PUBLISH_
    global _TRIGGER_GRANT_
    global _TRIGGER_CONFERENCE_
    global _TRIGGER_HIRE_

    _TRIGGER_PUBLISH_= 0
    _TRIGGER_GRANT_ = 1
    _TRIGGER_CONFERENCE_ = 2
    _TRIGGER_HIRE_ = 3
"""

trigger_dict = {
    "TRIGGER_PUBLISH"       : 1,
    "TRIGGER_HIRE"          : 2,
    "TRIGGER_GRANT"         : 3,
    "TRIGGER_CONFERENCE"    : 4,
    "TRIGGER_JOB_OFFER"     : 5,
    "TRIGGER_FAB_RESULTS"   : 6
    }



def trigger_happened(player, trigger, args):
    #print "%s has triggered %s!" % (player.name, trigger)
    other_player = get_other_player(player)
    for card in other_player.reactions.cards:
        if card.trigger == trigger:
            card.reveal(other_player, args)
            break


class Reaction(Card):
    def __init__(self, name, cost, description, trigger):
        super(Reaction, self).__init__(name, cost, description)
        self.trigger = trigger

    def play(self, player):
        # TODO: Add trigger
        super(Reaction, self).play(player)
        player.reactions.add_card(self)

    def reveal(self, player, args):
        player.reactions.remove_card(self)
        graveyard.add_card(self)

    def is_playable(self, player):
        if player.points >= self.cost and len(player.reactions.cards) < 3:
            return True
        else:
            return False

class Citation(Reaction):
    """ Apply to big grant card. Costs a lot but brings in lots of BP"""
    def __init__(self):
        name = 'Citation'
        cost = Points(1, 0, 0, 0, 0, 0)
        description = "You get half the other player's publication's IF. Cost: %s."\
                      %(cost.__repr__())
        super(Citation, self).__init__(name, cost, description, trigger_dict["TRIGGER_PUBLISH"])

    def reveal(self, player, args):
        """
        :param player: Player who is playing the card
        :return: True if success and False if failure
        """
        super(Citation, self).reveal(player, args)
        player.impact += args//2
        print("[REACT] The other player forces you to cite them!")


class AngryReferee(Reaction):
    """ Apply to big grant card. Costs a lot but brings in lots of BP"""
    def __init__(self):
        name = 'Angry Referee'
        cost = Points(5, 0, 0, 0, 0, 0)
        description = "Halves a publication's IF. Cost: %s."\
                      %(cost.__repr__())
        super(AngryReferee, self).__init__(name, cost, description, trigger_dict["TRIGGER_PUBLISH"])

    def reveal(self, player, args):
        """
        :param player: Player who is playing the card
        :return: True if success and False if failure
        """
        super(AngryReferee, self).reveal(player, args)
        other_player = get_other_player(player)
        other_player.impact -= args//2
        print("[REACT] An angry referee halves the impact factor of your publication!")


class Counterhire(Reaction):
    """ Apply to big grant card. Costs a lot but brings in lots of BP"""
    def __init__(self):
        name = 'Counterhire'
        cost = Points(5, 0, 0, 0, 0, 0)
        description = "Steals a new hire as it happens. Cost: %s."\
                      %(cost.__repr__())
        super(Counterhire, self).__init__(name, cost, description, trigger_dict["TRIGGER_HIRE"])

    def reveal(self, player, args):
        """
        :param player: Player who is playing the card
        :return: True if success and False if failure
        """
        super(Counterhire, self).reveal(player, args)
        other_player = get_other_player(player)
        other_player.unit.remove_card(args)
        player.unit.remove_card(args)
        print("[REACT] Your new hire went with to other unit! They received an offer they couldn't refuse...")


#gamedeck.add_card(Reaction("", Points(1, 0, 0, 0, 0, 0), "", trigger_dict["TRIGGER_HIRE"]))
