# terminalvelociraptor

This repository will be used during the Hackathingie event held at the OIST 
campus on January 7th and 8th, 2016. The goal of this project is to create a
terminal-based, academia-themed card game for future enjoyment.

We will further define the rules of the game and how we intend to complete the project during the event, so stay tuned!


*******************
* CODENAME MMOIST *
*******************

Ideas in the first "design document".

- Single deck for both players.

- Deck contains: Staff and Action cards.

- Players gain Budget Point Slots (BS) every turn (up to a maximum).

- Budget Points (BP) can be used to hire (play) Staff.

- Staff have Ability Points (Phys, Bio, ...).

- Ability Points can be used to play Action cards.

- Action cards can (for instance):
	* increase your maximum Budget Points available.
	* raise you Impact Factor.
	* increase number of Staff you can hire.
	* other things...

- The winner is:
	* The first to achieve X Impact Factor.
	* Other conditions (win Nobel Prize,...)
	
- Gameplay
    BEGIN
        * Randomise player order
        * Draw 5 cards each (from common pile)
        * Initial BS: 1 (1st player), 2 (2nd player)
       
    TURN
        * Gain 1 BS (up to a maximum of 5).  !! max val TBD
        * Renew BP (by filling up to current BS). 
        * Fire staff; pay staff.
        EITHER
            * Discard N cards from deck, and draw N-1 cards.
        OR
            * Play cards, as many as you want, up to existing AP and BP.
        * Cards to be discarded at any time, if number of cards in hand exceeds maximum of 10 cards. !! max TBD
        