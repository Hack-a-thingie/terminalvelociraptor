from defs import *
import random

def submit_manuscript(points):
    total = points.APG + points.APP + points.APC + points.APM + points.APB
    return total



gamedeck = CardPile()

zeropoints = Points(0, 0, 0, 0, 0, 0)
gamedeck.add_card(Card("Alice", zeropoints, ""))
gamedeck.add_card(Card("Bob", zeropoints, ""))
gamedeck.add_card(Card("Carmen", zeropoints, ""))
gamedeck.add_card(Card("David", zeropoints, ""))
gamedeck.add_card(Card("Eva", zeropoints, ""))
gamedeck.add_card(Card("Fabia", zeropoints, ""))
gamedeck.add_card(Card("Gabriel", zeropoints, ""))
gamedeck.add_card(Card("Herman", zeropoints, ""))
gamedeck.add_card(Card("Irina", zeropoints, ""))
gamedeck.add_card(Card("John", zeropoints, ""))
gamedeck.add_card(Card("Karl", zeropoints, ""))
gamedeck.add_card(Card("Louise", zeropoints, ""))
gamedeck.add_card(Card("Mark", zeropoints, ""))
gamedeck.add_card(Card("Nadia", zeropoints, ""))
gamedeck.add_card(Card("Oriol", zeropoints, ""))
gamedeck.add_card(Card("Pete", zeropoints, ""))
gamedeck.add_card(Card("Queco", zeropoints, ""))
gamedeck.add_card(Card("Ramon", zeropoints, ""))
gamedeck.add_card(Card("Sarah", zeropoints, ""))
gamedeck.add_card(Card("Tridib", zeropoints, ""))
gamedeck.add_card(Card("Ulrich", zeropoints, ""))
gamedeck.add_card(Card("Violeta", zeropoints, ""))
gamedeck.add_card(Card("Wolfgang", zeropoints, ""))
gamedeck.add_card(Card("Xavier", zeropoints, ""))
gamedeck.add_card(Card("Yahir", zeropoints, ""))
gamedeck.add_card(Card("Zelda", zeropoints, ""))

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

## FIRST TURN
# Gain 1 BS (up to a maximum of 5).  !! max val TBD
current_player.increase_bs_with_max(5)

# Renew BP (by filling up to current BS).
current_player.set_bp_to_bs()

# Fire staff; pay staff.
if current_player.get_staff_cost() < current_player.get_bp():
    print "Not enough, you have to fire someone"
    current_player.set_bp(0)
else:
    current_player.set_bp(current_player.get_bp() - current_player.get_staff_cost())

# EITHER Discard N cards from deck, and draw N-1 cards.

# OR Play cards, as many as you want, up to existing AP and BP.

# 'Submit manuscript' action (1BP)
submit_manuscript(zeropoints)

# Cards to be discarded at any time, if number of cards in hand exceeds maximum of 10 cards. !! max TBD

