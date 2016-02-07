from staff import *
from player import *
from cardpile import *
from actions import *
from reactions import *
from publish import *

import random

graveyard = CardPile()
gamedeck = Deck(graveyard)

zeropoints = Points(0, 0, 0, 0, 0, 0)
zeropoints = Points(1, 1, 1, 1, 1, 1)

gamedeck.add_card(Staff("Adi", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Bensi", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Carmen", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("David", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Eva", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Fabia", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Gabriel", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Herman", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Irina", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("James", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Karl", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Louise", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Mark", zeropoints, "Generic Physics undergrad", zeropoints))
gamedeck.add_card(Staff("Nadia", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Oriol", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Pete", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Queco", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Ramon", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Sarah", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Tridib", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Ulrich", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Violeta", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Wolfgang", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Xavier", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Yahir", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Zelda", zeropoints, "", zeropoints))

realplayer = Player("PLAYER")
computer = Player("CPU")


## INITIALISE GAME
# Shuffle deck
gamedeck.shuffle()

# Randomise player order
players = [realplayer, computer]
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
while not gamedeck.is_empty() and turn < 1000:
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

#   thing = raw_input("[d] discard OR [p] play: ")
#    thing = thing.lower()

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
        #for staff in current_player.unit.cards:
        #    print staff

    # 'Submit manuscript' action (1BP)
    #print submit_manuscript(current_player.get_staff_abilities())

print "\n\nGAME OVER\n\n"

print "deck: %s " % len(gamedeck.cards),
print "discard: %s " % len(graveyard.cards),
print "%s: (h=%d, u=%d) " % (realplayer.name, len(realplayer.hand.cards), len(realplayer.unit.cards)),
print "%s: (h=%d, u=%d) " % (computer.name, len(computer.hand.cards), len(computer.unit.cards))

total_cards = len(gamedeck.cards) + len(graveyard.cards) + len(realplayer.hand.cards) + len(realplayer.unit.cards) + len(computer.hand.cards) + len(computer.unit.cards)
print "TOTAL CARDS = %d" % total_cards

# Cards to be discarded at any time, if number of cards in hand exceeds maximum of 10 cards. !! max TBD

