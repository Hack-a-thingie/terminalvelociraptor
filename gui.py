#------------gui.py------------------------------------------------------------#

#            gui for academic terminal card game
#
# Purpose: This file has been created during the hack-a-thingie 2016 event and
#          will be using curses to create the terminal ui for playing the game.
#
#   Notes: importing game runs the game, fix this later.
#------------------------------------------------------------------------------#
#!/usr/local/bin/python2
# coding: latin-1

import curses
from game import *
from player import *
from deck import *
from cardpile import *
from staff import *
from actions import *
from reactions import *

#def print(str):
#    disp_message(str)

# displays a message, front and center!
def disp_message(message):
        while True:
            bg.addstr(11, int(59 / 2 - len(message) / 2), message)
            bgcomm = bg.getch()
            if bgcomm == ord(" "):
                for i in range(1,59):
                    bg.addch(11,i, curses.ACS_HLINE)
                    bg.refresh()
                break

# This function places BP, BS and all AP
def point_placement(BP, BS, phys, bio, chem, math, screen):
    if curses.has_colors() == True:

        # spacing between points
        coloffset = 5

        #index for column number
        colindex = 5 
        tmpstr = "BP: " + str(BP) + "/" + str(BS)
        screen.addstr(0, colindex, tmpstr)

        colindex = colindex + len(tmpstr) + coloffset

        tmpstr = "P: " + str(phys)
        screen.addstr(0, colindex, tmpstr, curses.color_pair(4))

        colindex = colindex + len(tmpstr) + coloffset

        tmpstr = "B: " + str(bio)
        screen.addstr(0, colindex, tmpstr, curses.color_pair(2))

        colindex = colindex + len(tmpstr) + coloffset

        tmpstr = "C: " + str(chem)
        screen.addstr(0, colindex, tmpstr, curses.color_pair(1))

        colindex = colindex + len(tmpstr) + coloffset

        tmpstr = "M: " + str(math)
        screen.addstr(0, colindex, tmpstr)

    screen.refresh()

# Chooses action
def choose_action(act, act_list, hand, hand_h, hand_w, bg, index):
    actidx = 1
    while True:
        playcomm = act.getch()
            
        if playcomm == ord("w"):
            act.addstr(0, 6, act_list[-1], curses.A_REVERSE | curses.A_BOLD)
            act.addstr(1, 6, act_list[2], curses.A_BOLD)
            act.move(0,6)
            actidx = 0
            act.refresh()
                
        if playcomm == ord("s"):
            act.addstr(0, 6, act_list[-1], curses.A_BOLD)
            act.addstr(1, 6, act_list[2], curses.A_REVERSE | curses.A_BOLD)
            act.move(1,6)
            actidx = 1
            act.refresh()

        if playcomm == ord(" "):
            act.addstr(0,6,"        ")
            act.addstr(1,6,act_list[1], curses.A_BOLD)
            if actidx == 0:
                for i in range(hand_w - 1):
                    for j in range(hand_h - 1):
                        hand.addch(j, i, " ")
                for i in range(len(handlist)):
                    if i == 0:
                        hand.addstr(i, 1, handlist[i], curses.A_REVERSE)
                    else:
                        hand.addstr(i, 1, handlist[i])
                hand.move(0,1)
                    
            elif actidx == 1:
                play_card(realplayer.hand.cards[index])
                #disp_message("yo")
                for i in range(hand_w - 1):
                    for j in range(hand_h - 1):
                        hand.addch(j, i, " ")
                for i in range(len(handlist)):
                    if i == 0:
                        hand.addstr(i, 1, handlist[i], curses.A_REVERSE)
                    else:
                        hand.addstr(i, 1, handlist[i])
                hand.move(0,1)

            act.refresh()
            break

# These are additional functions that must be implemented that I do not have
#def scroll_up();
#def scroll_down();

# creating dummy description:

description = "This card is awesome. it does a bunch of things and is super duper awesome and such."

# Setting up small-scale game data to work with
#staff = ["Bob", "Alice", "Quantum Crypt", '123456789012345678901234567890']
handlist = [realplayer.unit.cards[i].name 
            for i in range(len(realplayer.unit.cards))]

# Set up standard screen
bg = curses.initscr()
curses.start_color()
curses.use_default_colors()

for i in range(0, curses.COLORS):
    curses.init_pair(i, i, -1)

# Inhibits typing to screen
curses.noecho()

# No need for enter to use commands
curses.cbreak()

# Setting up keypad usage
bg.keypad(1)

bg_x = 0
bg_y = 0
bg_h = 24
bg_w = 80
bg = curses.newwin(bg_h, bg_w, bg_y, bg_x)

#------------------------------------------------------------------------------#
# Background and Hand Selection
#------------------------------------------------------------------------------#
# Note: handlist may change form

# Defining corners
bg.addch(0, 0, curses.ACS_ULCORNER)
bg.addch(23, 0, curses.ACS_LLCORNER)
bg.addch(0, curses.COLS - 2, curses.ACS_URCORNER)
bg.addch(23, curses.COLS - 2, curses.ACS_LRCORNER)

# Defining borders
center_hline = 11
vline = 59

# We need to change the names of the staff to fit into our box:
for i in range(len(handlist)):
    if len(handlist[i]) < 76 - vline:
        for j in range(76 - vline - len(handlist[i])):
            handlist[i] = handlist[i] + ' '
    elif len(handlist[i]) > 76 - vline:
        handlist[i] = handlist[i][0:76 - vline]

for i in range(1,curses.COLS-2):
    bg.addch(0, i, curses.ACS_HLINE)
    bg.addch(23, i, curses.ACS_HLINE)

    # Drawing hlines
    if i < vline:
        bg.addch(center_hline, i, curses.ACS_HLINE)
        bg.addch(21, i, curses.ACS_HLINE)
        bg.addch(19, i, curses.ACS_HLINE)
        bg.addch(2, i, curses.ACS_HLINE)
        bg.addch(4, i, curses.ACS_HLINE)

    if i > vline:
        bg.addch(20, i, curses.ACS_HLINE)

    # Drawing vlines
    if i <= 22:
        bg.addch(i, 0, curses.ACS_VLINE)
        bg.addch(i, curses.COLS - 2, curses.ACS_VLINE)
        bg.addch(i, vline, curses.ACS_VLINE)

    # Adding corners Top and Bottom
    if i == vline:
        bg.addch(0, vline, curses.ACS_TTEE)
        bg.addch(23, vline, curses.ACS_BTEE)

    # Adding corners Left and Right
    if i == center_hline or i == 21 or i == 19 or i == 2 or i == 4:
        bg.addch(i, 0, curses.ACS_LTEE)
        bg.addch(i, vline, curses.ACS_RTEE)

    if i == 20:
        bg.addch(i, vline, curses.ACS_LTEE)
        bg.addch(i, curses.COLS - 2, curses.ACS_RTEE)

bg.refresh()

# Add in a window for hand cards
hand_x = vline + 1
hand_y = 1
hand_h = 23 - 5
hand_w = 18
hand = curses.newwin(hand_h, hand_w, hand_y, hand_x)

hand.move(0, 0)

index = 0
for i in range(len(handlist)):
    if i == 0:
        hand.addstr(i, 1, handlist[i], curses.A_REVERSE)
    else:
        hand.addstr(i, 1, handlist[i])

#------------------------------------------------------------------------------#
# Passive Windows
#------------------------------------------------------------------------------#

# First, the window with "ACTION" in it
act_x = vline + 1
act_y = 23 - 2
act_h = 2
act_w = 18
act = curses.newwin(act_h, act_w, act_y, act_x)

# creating an act_string list
act_list = ['ACTION ', 'SELECT ', ' PLAY  ', 'DISCARD', 'RETURN']
act_str = act_list[1]

act.addstr(1, 6, act_str, curses.A_BOLD)
act.refresh()

# Now to implement the Impact Factor bars, 50 cols total
# These will be implemented as highlighted bars, no biggie

# Opponent first, because we are gentlemen

oppif_x = 1
oppif_y = 1
oppif_h = 1
oppif_w = vline - 1

oppif = curses.newwin(oppif_h, oppif_w, oppif_y, oppif_x)

oppif.addstr(0,1,"IF: [")
oppif.addch(0, vline - 3 , "]")

# Now to fill the IF bar with stuff (fake IF percent)
oppif_percent = computer.impact / 20
oppif_col = int(oppif_percent * 50)
for i in range(50):
    if i < oppif_col:
        oppif.addch(0,i+6," ", curses.A_STANDOUT)

oppif.refresh()

# Now for my IF

meif_x = 1
meif_y = 22
meif_h = 1
meif_w = vline - 1

meif = curses.newwin(meif_h, meif_w, meif_y, meif_x)

meif.addstr(0,1,"IF: [")
meif.addch(0, vline - 3 , "]")

# Now to fill the IF bar with stuff (fake IF percent)
meif_percent = realplayer.impact
meif_col = int(meif_percent * 50)
for i in range(50):
    if i < meif_col:
        meif.addch(0,i+6," ", curses.A_STANDOUT)

meif.refresh()

# Now to update the points

opppt_x = 1
opppt_y = 3
opppt_h = 1
opppt_w = vline - 1

opppt = curses.newwin(opppt_h, opppt_w, opppt_y, opppt_x)

# Setting up Budget, Physics, Bio, Chem, and math with colors
oppbp = computer.points.BP
oppbs = computer.bs
oppphys = computer.points.APP
oppbio = computer.points.APB
oppchem = computer.points.APB
oppmath = computer.points.APM

point_placement(oppbp, oppbs, oppphys, oppbio, oppchem, oppmath, opppt)

mept_x = 1
mept_y = 20
mept_h = 1
mept_w = vline - 1

mept = curses.newwin(mept_h, mept_w, mept_y, mept_x)

# Setting up Budget, Physics, Bio, Chem, and math with colors
mebp = realplayer.points.BP
mebs = realplayer.bs
mephys = realplayer.points.APP
mebio = realplayer.points.APB
mechem = realplayer.points.APC
memath = realplayer.points.APM

point_placement(mebp, mebs, mephys, mebio, mechem, memath, mept)

#------------------------------------------------------------------------------#
# Hand Cursor Movement
#------------------------------------------------------------------------------#

index = 0
prev = 0
hand.move(0,1)

while True:
    command = hand.getch()
    if command == ord("w"):
        prev = index
        index = index - 1
        if index < 0:
            index = 0
        hand.addstr(index, 1, handlist[index], curses.A_REVERSE)
        hand.addstr(prev, 1, handlist[prev])
        hand.move(index,1)
        hand.refresh()

    if command == ord("s"):
        prev = index
        index = index + 1
        if index >= len(handlist):
            index = len(handlist) - 1
        hand.addstr(index, 1, handlist[index], curses.A_REVERSE)
        hand.addstr(prev, 1, handlist[prev])
        hand.move(index,1)
        hand.refresh()

    if command == ord(" "):
        if act_str == act_list[1]:
            # prints description
            act.addstr(0, 6, act_list[-1], curses.A_BOLD)
            act.addstr(1, 6, act_list[2], curses.A_BOLD | curses.A_REVERSE)   
            act.refresh()
            hand.addstr(0, 1, handlist[index], curses.A_REVERSE)
            for i in range(77-vline):
                hand.addch(1,i, curses.ACS_HLINE)
            words = description.split()
            desc_idx = 0
            line = ""
            for word in words:
                if len(line) + len(word) + 1 < 76-vline:
                    line = line + word + " "
                    if word == words[-1]:
                        hand.addstr(2 + desc_idx, 1, line)
                else:
                    for i in range (76-vline-len(line)):
                        line = line + " "
                    hand.addstr(2 + desc_idx, 1, line)
                    line = word + " "
                    desc_idx = desc_idx + 1
                    if word == words[-1]:
                        hand.addstr(2 + desc_idx, 1, line)

            hand.refresh()
            act_str = act_list[1]

            act.move(1,6)
            choose_action(act, act_list, hand, hand_h, hand_w, bg, index)
            index = 0
            prev = 0

        else:
            act.addstr(1, 6, act_str, curses.A_BOLD)   
            act.refresh()
            act_str = act_list[1]
        

    if command == ord("q"):
        break
bg.getch()

# Terminating curses:
curses.nocbreak()
bg.keypad(0)
curses.echo()
curses.endwin()
