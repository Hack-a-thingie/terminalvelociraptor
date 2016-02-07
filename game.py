from staff import *
from player import *
from cardpile import *
from actions import *
from reactions import *
from publish import *

from deck import *

import random


realplayer = Player("PLAYER")
computer = Player("CPU")

players.append(realplayer)
players.append(computer)


## INITIALISE GAME

# Initialise deck
graveyard = CardPile()
gamedeck = Deck(graveyard)

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
while not gamedeck.is_empty() and turn < 1000 and not won:
    turn += 1
    current_player = players[turn % 2]

    print "\n TURN %d: %s" % (turn, current_player.name)

    print "deck: %s " % len(gamedeck.cards),
    print "discard: %s " % len(graveyard.cards),
    print "%s: (h=%d, u=%d) " % (realplayer.name, len(realplayer.hand.cards), len(realplayer.unit.cards)),
    print "%s: (h=%d, u=%d) " % (computer.name, len(computer.hand.cards), len(computer.unit.cards))

    total_cards = len(gamedeck.cards) + len(graveyard.cards) + len(realplayer.hand.cards) + len(realplayer.unit.cards) + len(computer.hand.cards) + len(computer.unit.cards)
    print "TOTAL CARDS = %d" % total_cards

    # Gain 1 BS (up to a maximum of 5).  !! max val TBD
    current_player.increase_bs_with_max(5)

    # Renew BP (by filling up to current BS).
    current_player.set_bp_to_bs()

    # Fire staff; pay staff.
    if current_player.get_staff_cost() > current_player.points.BP:
        while current_player.get_staff_cost() > current_player.points.BP:
            print "Not enough, you have to fire someone"
            current_player.fire_someone(graveyard)

    current_player.points.BP = current_player.points.BP - current_player.get_staff_cost()

    # Draw a card.
    current_player.draw_card(gamedeck)

    # if current_player is realplayer:
    #     thing = raw_input("[d] discard OR [p] play: ")
    #     thing = thing.lower()
    # else:
    thing = random.choice(["p", "d"])

    if thing == "d":
        # EITHER Discard N cards from deck, and draw N-1 cards.
        n_cards_discard = random.randrange(len(current_player.hand.cards)-1)+1
        print "Discarding %d cards" % n_cards_discard
        for i in range(n_cards_discard):
            current_player.discard_card(graveyard)
            print "%s %s" % (i, len(current_player.hand.cards))

        for i in range(n_cards_discard-1):
            current_player.draw_card(gamedeck)

    elif thing == "p":
        # OR Play cards, as many as you want, up to existing AP and BP.
        print "Playing card"
        current_player.hand.cards[0].play(current_player)
        for staff in current_player.unit.cards:
            print staff

    # 'Submit manuscript' action (1BP)

    # if current_player is realplayer:
    #     thing = raw_input("Do you want to publish your.. 'results'? (1 BP) [y] yes OR [n] no: ")
    #     thing = thing.lower()
    # else:
    thing = random.choice(["y", "n"])

    if thing == "y":
        if current_player.points.BP > 0:
            current_player.impact += submit_manuscript(current_player.get_staff_abilities());
            trigger_happened(current_player,trigger_dict["TRIGGER_PUBLISH"])
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

print "deck: %s " % len(gamedeck.cards),
print "discard: %s " % len(graveyard.cards),
print "%s: (h=%d, u=%d) " % (realplayer.name, len(realplayer.hand.cards), len(realplayer.unit.cards)),
print "%s: (h=%d, u=%d) " % (computer.name, len(computer.hand.cards), len(computer.unit.cards))

total_cards = len(gamedeck.cards) + len(graveyard.cards) + len(realplayer.hand.cards) + len(realplayer.unit.cards) + len(computer.hand.cards) + len(computer.unit.cards)
print "TOTAL CARDS = %d" % total_cards

# Cards to be discarded at any time, if number of cards in hand exceeds maximum of 10 cards. !! max TBD

