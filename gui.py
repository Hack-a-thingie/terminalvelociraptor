#------------gui.py------------------------------------------------------------#
#
#            gui for academic terminal card game
#
# Purpose: This file has been created during the hack-a-thingie 2016 event and
#          will be using curses to create the terminal ui for playing the game.
#
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
hline = 11
vline = 59
for i in range(1,79):
    stdscreen.addch(0,i, curses.ACS_HLINE)
    stdscreen.addch(23, i, curses.ACS_HLINE)
    if i < vline:
        stdscreen.addch(hline, i, curses.ACS_HLINE)
    if i <= 22:
        stdscreen.addch(i, 0, curses.ACS_VLINE)
        stdscreen.addch(i, 78, curses.ACS_VLINE)
        stdscreen.addch(i, vline, curses.ACS_VLINE)
    if i == vline:
        stdscreen.addch(0, vline, curses.ACS_TTEE)
        stdscreen.addch(23, vline, curses.ACS_BTEE)
    if i == hline:
        stdscreen.addch(i, 0, curses.ACS_LTEE)
        stdscreen.addch(i, vline, curses.ACS_RTEE)
        
stdscreen.getch()

# Terminating curses:
curses.nocbreak()
stdscreen.keypad(0)
curses.echo()
curses.endwin()
