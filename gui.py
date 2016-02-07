#------------gui.py------------------------------------------------------------#
#
#            gui for academic terminal card game
#
# Purpose: This file has been created during the hack-a-thingie 2016 event and
#          will be using curses to create the terminal ui for playing the game.
#
#   Notes: We need to implement the following:
#              Hand, field, description, points
#              functions by click
#------------------------------------------------------------------------------#
#!/usr/local/bin/python2
# coding: latin-1

import curses

# Setting up small-scale game data to work with
staff = ["Bob", "Alice", "Quantum Crypt", '123456789012345678901234567890']

# Set up standard screen
bg = curses.initscr()

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
# Note: stafflist may change form

# Defining corners
bg.addch(0, 0, curses.ACS_ULCORNER)
bg.addch(23, 0, curses.ACS_LLCORNER)
bg.addch(0, curses.COLS - 2, curses.ACS_URCORNER)
bg.addch(23, curses.COLS - 2, curses.ACS_LRCORNER)

# Defining borders
center_hline = 11
vline = 59

# We need to change the names of the staff to fit into our box:
stafflist = staff
for i in range(len(stafflist)):
    if len(stafflist[i]) < 76 - vline:
        print ("found")
        for j in range(76 - vline - len(stafflist[i])):
            print(j)
            stafflist[i] = stafflist[i] + ' '
    elif len(stafflist[i]) > 76 - vline:
        stafflist[i] = stafflist[i][0:76 - vline]

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

# Placing Action command
#bg.addstr(22, 66, "ACTION", curses.A_BOLD)

bg.refresh()

# Add in a window for hand cards
hand_x = vline + 1
hand_y = 1
hand_h = 23 - 5
hand_w = 18
hand = curses.newwin(hand_h, hand_w, hand_y, hand_x)

hand.move(0, 0)

index = 0
for i in range(len(stafflist)):
    if i == 0:
        hand.addstr(i, 1, stafflist[i], curses.A_REVERSE)
    else:
        hand.addstr(i, 1, stafflist[i])

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
act_list = ['ACTION ', 'SELECT ', ' PLAY  ', 'DISCARD']
act_str = act_list[1]

act.addstr(1, 6, act_str, curses.A_BOLD)
act.refresh()

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
        hand.addstr(index, 1, stafflist[index], curses.A_REVERSE)
        hand.addstr(prev, 1, stafflist[prev])
        hand.move(index,1)
        hand.refresh()

    if command == ord("s"):
        prev = index
        index = index + 1
        if index >= len(stafflist):
            index = len(stafflist) - 1
        hand.addstr(index, 1, stafflist[index], curses.A_REVERSE)
        hand.addstr(prev, 1, stafflist[prev])
        hand.move(index,1)
        hand.refresh()

    if command == ord(" "):
        if act_str == act_list[1]:
            act.addstr(1, 6, act_str, curses.A_BOLD)   
            act.refresh()
            act_str = act_list[2]
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
