#------------gui.py------------------------------------------------------------#
#
#            gui for academic terminal card game
#
# Purpose: This file has been created during the hack-a-thingie 2016 event and
#          will be using curses to create the terminal ui for playing the game.
#
#------------------------------------------------------------------------------#

import curses

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

stdscreen.addstr(1,12, "Help me!")

stdscreen.getch()

# Terminating curses:
curses.nocbreak()
stdscreen.keypad(0)
curses.echo()
curses.endwin()
