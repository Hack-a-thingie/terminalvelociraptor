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

import curses
import _curses

# Set up standard screen
stdscreen = curses.initscr()

# Inhibits typing to screen
curses.noecho()

# No need for enter to use commands
curses.cbreak()

# Setting up keypad usage
stdscreen.keypad(1)

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

# Defining corners
stdscreen.addch(0,0, curses.ACS_ULCORNER)
stdscreen.addch(23,0, curses.ACS_LLCORNER)
stdscreen.addch(0,78, curses.ACS_URCORNER)
stdscreen.addch(23,78, curses.ACS_LRCORNER)

# Defining borders
center_hline = 11
vline = 59
for i in range(1,78):
    stdscreen.addch(0,i, curses.ACS_HLINE)
    stdscreen.addch(23, i, curses.ACS_HLINE)

    # Drawing hlines
    if i < vline:
        stdscreen.addch(center_hline, i, curses.ACS_HLINE)
        stdscreen.addch(21, i, curses.ACS_HLINE)
        stdscreen.addch(19, i, curses.ACS_HLINE)
        stdscreen.addch(2, i, curses.ACS_HLINE)
        stdscreen.addch(4, i, curses.ACS_HLINE)

    if i > vline:
        stdscreen.addch(20, i, curses.ACS_HLINE)

    # Drawing vlines
    if i <= 22:
        stdscreen.addch(i, 0, curses.ACS_VLINE)
        stdscreen.addch(i, 78, curses.ACS_VLINE)
        stdscreen.addch(i, vline, curses.ACS_VLINE)

    # Adding corners Top and Bottom
    if i == vline:
        stdscreen.addch(0, vline, curses.ACS_TTEE)
        stdscreen.addch(23, vline, curses.ACS_BTEE)

    # Adding corners Left and Right
    if i == center_hline or i == 21 or i == 19 or i == 2 or i == 4:
        stdscreen.addch(i, 0, curses.ACS_LTEE)
        stdscreen.addch(i, vline, curses.ACS_RTEE)

    if i == 20:
        stdscreen.addch(i, vline, curses.ACS_LTEE)
        stdscreen.addch(i, 78, curses.ACS_RTEE)

# Placing Action command
stdscreen.addstr(22, 67, "ACTION", curses.A_BOLD)

stdscreen.getch()

# Terminating curses:
curses.nocbreak()
stdscreen.keypad(0)
curses.echo()
curses.endwin()
