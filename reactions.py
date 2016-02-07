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
    "TRIGGER_JOB_OFFER"     : 5
    }


def get_other_player(player):
    for other_player in players:
        if not other_player is player:
            return other_player


def trigger_happened(player, trigger, args):
    #print "%s has triggered %s!" % (player.name, trigger)
    other_player = get_other_player(player)
    for card in other_player.reactions.cards:
        if card.trigger == trigger:
            card.reveal(other_player, args)


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
        print("An angry referee halves the impact factor of your publication!")


#gamedeck.add_card(Reaction("I'm gonna make him an offer he can't refuse", Points(1, 0, 0, 0, 0, 0), "", trigger_dict["TRIGGER_HIRE"]))
