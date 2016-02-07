import defs
from player import *
"""This file contains the functionality of the Reaction cards"""

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
    "TRIGGER_GRANT"         : 2,
    "TRIGGER_CONFERENCE"    : 3,
    "TRIGGER_HIRE"          : 4
    }

def trigger_happened(player, trigger):
    print "%s has triggered %s!" % (player.name, trigger)


class Reaction(Card):
    def __init__(self, name, cost, description, trigger, effect):
        super(Reaction, self).__init__(name, cost, description)
        self.trigger = trigger
        self.effect = effect

    def play(self, player):
        # ...
        pass
