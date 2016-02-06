from staff import *
from player import *
from cardpile import *

import random

def submit_manuscript(points):
    total = points.APG + points.APP + points.APC + points.APM + points.APB
    return total



gamedeck = CardPile()

zeropoints = Points(0, 0, 0, 0, 0, 0)
zeropoints = Points(1, 1, 1, 1, 1, 1)

gamedeck.add_card(Staff("Adi", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Bob", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Carmen", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("David", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Eva", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Fabia", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Gabriel", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Herman", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("Irina", zeropoints, "", zeropoints))
gamedeck.add_card(Staff("John", zeropoints, "", zeropoints))
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

realplayer = Player()
computer = Player()


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

current_player = players[0]



## TURN

while not gamedeck.is_empty():
    print "Cards in deck: %s" % len(gamedeck.cards)
    print "Cards in realplayer hand: %s" % len(realplayer.hand.cards)
    print "Cards in computer hand: %s" % len(computer.hand.cards)

    # Gain 1 BS (up to a maximum of 5).  !! max val TBD
    current_player.increase_bs_with_max(5)

    # Renew BP (by filling up to current BS).
    current_player.set_bp_to_bs()


    # Fire staff; pay staff.
    if current_player.get_staff_cost() > current_player.points.BP:
        print "Not enough, you have to fire someone"
        current_player.points.BP = 0
        current_player.unit.cards.pop(0)
    else:
        current_player.points.BP = current_player.points.BP - current_player.get_staff_cost()

    # Draw a card.
    current_player.draw_card(gamedeck)


    #todo = raw_input("[d] discard OR [p] play: ")
    todo = "p"
    todo = todo.lower()
    if todo == "d":
        # EITHER Discard N cards from deck, and draw N-1 cards.
        print "DISCARD"
        current_player.hand.cards.pop(0)
    elif todo == "p":
        # OR Play cards, as many as you want, up to existing AP and BP.
        print "PLAY"
        current_player.hand.cards[0].play(current_player)

    # 'Submit manuscript' action (1BP)
    print type(current_player.get_staff_abilities())
    print submit_manuscript(current_player.get_staff_abilities())

print "GAME OVER"
# Cards to be discarded at any time, if number of cards in hand exceeds maximum of 10 cards. !! max TBD

