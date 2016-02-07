"""
Definition of various classes
"""


class Points(object):
    """Contains all information regarding in-game points - action points and budget points."""
    def __init__(self, BP, APG, APP, APC, APM, APB):
        self.BP = BP    # Budget Points
        self.APG = APG  # Action Points: General
        self.APP = APP  # Action Points: Physics
        self.APC = APC  # Action Points: Chemistry
        self.APM = APM  # Action Points: Mathematics
        self.APB = APB  # Action Points: Biology

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __add__(self, other):
        return Points(self.BP + other.BP,
                      self.APG + other.APG,
                      self.APP + other.APP,
                      self.APC + other.APC,
                      self.APM + other.APM,
                      self.APB + other.APB)

    def __sub__(self, other):
        return Points(self.BP - other.BP,
                      self.APG - other.APG,
                      self.APP - other.APP,
                      self.APC - other.APC,
                      self.APM - other.APM,
                      self.APB - other.APB)

    def __repr__(self):
        """ Convert the structure into an intelligible string. """
        return "BP: %d, APG: %d, APP: %d, "\
               "APC: %d, APM: %d, APB: %d"\
               % (self.BP, self.APG, self.APP, self.APC, self.APM, self.APB)

    def __ge__(self, other):
        """
        Overload >= operator
        """
        return self.APB >= other.APB and self.APM >= other.APM and self.APC >= other.APC and \
               self.APG >= other.APG and self.APP >= other.APP and self.BP >= other.BP


class Card(object):
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

    def play(self, player):
        if self.is_playable(player):
            player.remove_from_hand(self)
            player.points -= self.cost

    def is_playable(self, player):
        """
        :param player: The player who is attempting to play the card
        :return: True if the card is ok to play and False otherwise
        """
        return True if player.points >= self.cost else False
