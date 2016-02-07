#------------gui.py------------------------------------------------------------#

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


import curses

# Setting up small-scale game data to work with
staff = ["Bob", "Alice", "Quantum Crypt", '123456789012345678901234567890']

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
oppif_percent = 0.25
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
meif_percent = 1.0
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
oppbp = 10
oppbs = 20
oppphys = 5
oppbio = 10
oppchem = 17
oppmath = 7

point_placement(oppbp, oppbs, oppphys, oppbio, oppchem, oppmath, opppt)

mept_x = 1
mept_y = 20
mept_h = 1
mept_w = vline - 1

mept = curses.newwin(mept_h, mept_w, mept_y, mept_x)

# Setting up Budget, Physics, Bio, Chem, and math with colors
mebp = 10
mebs = 20
mephys = 5
mebio = 10
mechem = 17
memath = 7

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
