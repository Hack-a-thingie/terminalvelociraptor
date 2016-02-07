import math
import random
from defs import *
from cardpile import *
from staff import *
from actions import *
from reactions import *
from player import *
from publish import *
from deck import *

def count_cards():
    print "deck: %s " % len(gamedeck.cards),
    print "discard: %s " % len(graveyard.cards),
    print "%s: (h=%d, u=%d) " % (realplayer.name, len(realplayer.hand.cards), len(realplayer.unit.cards)),
    print "%s: (h=%d, u=%d) " % (computer.name, len(computer.hand.cards), len(computer.unit.cards))

    total_cards = len(gamedeck.cards) + len(graveyard.cards) + \
                  len(realplayer.hand.cards) + len(realplayer.unit.cards) + len(realplayer.reactions.cards) \
                  + len(computer.hand.cards) + len(computer.unit.cards) + len(computer.reactions.cards)
    print "TOTAL CARDS = %d" % total_cards


def rand_points(n):
    p = random.randint(0, n+1)
    c = random.randint(0, n+1-p)
    m = random.randint(0, n+1-p-c)
    b = random.randint(0, n+1-p-c-m)
    return Points(0, n, p, c, m, b)


def initialise_deck(gamedeck):
    zerocost = Points(0, 0, 0, 0, 0, 0)
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
    for i in range(5):
        gamedeck.add_card(SmallGrant())
        gamedeck.add_card(MediumGrant())
        gamedeck.add_card(BigGrant())
        gamedeck.add_card(Workshop())
        gamedeck.add_card(Symposium())
        gamedeck.add_card(Conference())
        gamedeck.add_card(RealJobOffer())
        gamedeck.add_card(FabricateResults())
    for i in range(5):
        gamedeck.add_card(AngryReferee())
        gamedeck.add_card(Counterhire())
        gamedeck.add_card(Citation())



realplayer = Player("PLAYER")
computer = Player("CPU")

players.append(realplayer)
players.append(computer)




## INITIALISE GAME

# Initialise deck
initialise_deck(gamedeck)

gamedeck.shuffle()

# Game not won
won = 0

# Randomise player order
random.shuffle(players)

# Draw 5 cards each (from common pile)
for player in players:
    for i in range(5):
        player.draw_card(gamedeck)

# Initial BS: 1 (1st player), 2 (2nd player)
players[0].bs = 1
players[1].bs = 2


# TURN
turn = 0
while turn < 5000 and not won:
    turn += 1
    current_player = players[turn % 2]

    print "\n TURN %d: %s" % (turn, current_player.name)

    count_cards()
    print "IFs:(%d, %d)" % (realplayer.impact, computer.impact)

    # Gain 1 BS (up to a maximum of 5).  !! max val TBD
    current_player.increase_bs_with_max(5)

    # Renew BP (by filling up to current BS).
    current_player.set_points_to_staff_and_bs()
    print current_player.points

    # Fire staff; pay staff.
    if current_player.get_staff_cost() > current_player.points.BP:
        while current_player.get_staff_cost() > current_player.points.BP:
            print "Not enough, you have to fire someone"
            current_player.fire_someone(graveyard)

    current_player.points.BP = current_player.points.BP - current_player.get_staff_cost()
    current_player.get_staff_abilities()

    # Draw a card.
    current_player.draw_card(gamedeck)

    # if current_player is realplayer:
    #     thing = raw_input("[d] discard OR [p] play: ")
    #     thing = thing.lower()
    # else:
    thing = "p"#random.choice(["p", "d"])

    if thing == "d":
        # EITHER Discard N cards from deck, and draw N-1 cards.
        n_cards_discard = random.randrange(len(current_player.hand.cards)-1)+1
        print "Discarding %d cards" % n_cards_discard
        for i in range(n_cards_discard):
            current_player.discard_card()
            #print "%s %s" % (i, len(current_player.hand.cards))

        for i in range(n_cards_discard-1):
            current_player.draw_card(gamedeck)

    elif thing == "p":
        # OR Play cards, as many as you want, up to existing AP and BP.
        selected_card = random.choice(current_player.hand.cards)
        if selected_card.is_playable(current_player):
            print "Playing card %s" % selected_card.name
            selected_card.play(current_player)
            #for staff in current_player.unit.cards:
            #    print staff
        else:
            print "Can't play card %s" % selected_card.name

    # 'Submit manuscript' action (1BP)

    # if current_player is realplayer:
    #     thing = raw_input("Do you want to publish your.. 'results'? (1 BP) [y] yes OR [n] no: ")
    #     thing = thing.lower()
    # else:
    thing = random.choice(["y", "n"])

    if thing == "y":
        if current_player.points.BP > 0:
            journal_impact = submit_manuscript(player.points)
            current_player.impact += journal_impact
            trigger_happened(current_player, trigger_dict["TRIGGER_PUBLISH"], journal_impact)
        else:
            print "Not enough budget."

    elif thing == "n":
        print "And you're calling yourself a PI.."

    print "%s has now %d IF" % (current_player.name, current_player.impact)

    # Win check
    for player in players:
        if player.impact >= 20:
            won = 1
            print "%s has won since it now has %d IF. Woo!.." % (player.name, player.impact)

        if player.bs == 0:
            won = 1
            print "%s has lost as ran out of budget. Boo!.." % player.name

print "\n\nGAME OVER\n\n"

count_cards()
print "IFs:(%d, %d)" % (realplayer.impact, computer.impact)

# Cards to be discarded at any time, if number of cards in hand exceeds maximum of 10 cards. !! max TBD

