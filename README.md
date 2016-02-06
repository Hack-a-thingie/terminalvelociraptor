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

- There are different kinds of Staff (even though these are just names and have no effect on gameplay):
    * Undergrad             [AP: 1   / BP: 2  / #: 4]
    * PhD student           [AP: 2,3 / BP: 3  / #: 3]
    * Postdoc               [AP: 3,4 / BP: 6  / #: 2]
    * Staff scientist       [AP: 4,5 / BP: 10 / #: 1]

    Others that we might include later (or a few now)
    * MSc student [between Undergrad and PhD student]
    * Technician [similar to Postdoc]
    * Visitor [it can really be anything, usually for a few turns]
    * Research assistant [0 AP, but cool passive/active abilities]

- Staff have Ability Points, which belong to 4 fields [associated to kind of different play styles]:
    * Physics   (blue)  [increase Budget Slots]
    * Chemistry (red)   [powerful attacks]
    * Biology   (green) [higher Impact Factor]
    * Maths     (white) [lots of low level staff]

    Others we might include later are:
    * Computer science
    * Crackpot science

- Ability Points can be used to play Action cards.

- Categories of Action cards can be:
	* Gain IF
	    [Conference] (could add temporal passive effects)
	        1 BP + 2 AP -> 1 IF
	        2 BP + 3 AP -> 3 IF
	* Grants
	    [Big Grant] (req. min 5 staff)
	        10 AP -> 2 BS + 3 IF + 2 BP
	        15 AP -> 4 BS + 6 IF + 4 BP
	    [Small Grant] (req. min 1 staff)
	         3 AP -> 1 IF + 2 BP
	* "Attacks"
	    [Real job offer]    8 BP + 2 AP (kill staff)
	    [Fabricate results] 10 AP (decrease 5 IF)
	    [Lab explosion]     1 BP + 15 AP (decrease 1 BS)
	    [Illness]           1 BP + 10 AP (disable staff) (permanent/temporary)
	    [Distract]          1 BP + 5 AP (halve (round down) AP of staff) (permanent/temporary)
	* Reaction cards (you can play 3 and have them ready to react to things your opponent does)
	    [Angry referee]     2 BP + 4 AP (halves gain in IF)
	    [Tag along]         3 BP (if other player goes to conference, you get the same effects)
        [Counterhire]       # BP (can hire other player's hire of cost < #)
	    [Cite me!]          5 AP + 1 BP (other player publishes, you get their gain in IF/2)
	    [Deny grant]        5 BP
	    [Deny publication]  4 BP
	    [Deny conference]   3 BP
	    [Deny hire]         2 BP

	
- Gameplay
    BEGIN
        * Randomise player order
        * Draw 5 cards each (from common pile)
        * Initial BS: 1 (1st player), 2 (2nd player)
       
    TURN
        * Gain 1 BS (up to a maximum of 5).  !! max val TBD
        * Renew BP (by filling up to current BS). 
        * Fire staff; pay staff.
        * Draw a card.
        EITHER
            * Discard N cards from deck, and draw N-1 cards.
        OR
            * Play cards, as many as you want, up to existing AP and BP.
        * 'Submit manuscript' action (1BP): main method of gaining IF.
          Starting with high IF journals, and going down, randomly you publish or not, depending on added AP.
        * Cards to be discarded at any time, if number of cards in hand exceeds maximum of 10 cards. !! max TBD

- End of game
	* When a player reaches an Impact Factor of 30, they win.
	* If a player reaches 0 Budget Slots.

