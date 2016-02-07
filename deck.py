from defs import *
from cardpile import *
from staff import *
from numpy import random

class Deck(CardPile):
    def __init__(self, discardpile):
        super(Deck, self).__init__()
        self.discardpile = discardpile

    def get_first_card(self):
        if self.is_empty():
            print "HOW DID THIS HAPPEN?"
        else:
            card_to_give = self.cards.pop(0)

        if self.is_empty():
            self.discardpile.shuffle()
            while not self.discardpile.is_empty():
                self.add_card(self.discardpile.cards.pop(0))

        return card_to_give


def rand_points(n):
    p = random.randint(0, n+1)
    c = random.randint(0, n+1-p)
    m = random.randint(0, n+1-p-c)
    b = random.randint(0, n+1-p-c-m)
    return Points(0, n, p, c, m, b)


def initialise_deck(gamedeck):
    zeropoints = Points(0, 0, 0, 0, 0, 0)
    onecost = Points(1, 0, 0, 0, 0, 0)

    gamedeck.add_card(Staff("Adi", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Bensi", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Carmen", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("David", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Eva", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Fabia", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Gabriel", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Herman", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Irina", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("James", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Karl", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Lee", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Mark", onecost, "Generic Physics undergrad", rand_points(4)))
    gamedeck.add_card(Staff("Nadia", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Oriol", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Pete", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Queco", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Ramon", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Sarah", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Thomas", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Ulrich", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Valentin", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Wolfgang", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Xavier", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Yahir", onecost, "", rand_points(4)))
    gamedeck.add_card(Staff("Zelda", onecost, "", rand_points(4)))
    for i in range(25):
        gamedeck.add_card(Reaction("Angry Referee", Points(0, 0, 0, 0, 0, 0), "", trigger_dict["TRIGGER_PUBLISH"], "I'M ANGRY!!!"))
        gamedeck.add_card(Reaction("I'm gonna make him an offer he can't refuse", Points(0, 0, 0, 0, 0, 0), "", trigger_dict["TRIGGER_HIRE"], "HIRE BLOCK!"))