############################################################################################
# Date:    2nd Jan, 2018                  # TimesTable is a game that my 6yo daughter used #
# Author:  Tiberiu Gociu                  # to play to learn the ... times table! :)       #
# Project: Times Table self playing game  # This exercise is to have a program that plays  #
#          using curses library           # with itself and creates data for future use.   #
############################################################################################
# CURSES uses teh Y,X coordinates         #
###########################################

import curses
import numpy 
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

from random import randint

# initialize the screen
curses.initscr()
# define the screen size
win = curses.newwin(20, 60, 0, 0)
# curses interprets input from keyboard
win.keypad(1)
# Leave echo mode. Echoing of input characters is turned off.
curses.noecho()
# Set the cursor state. visibility can be set to 0, 1, or 2, for invisible, normal, or very visible.
curses.curs_set(0)
# Draws a border around the screen
win.border(0)
# If yes is 1, getch() will be non-blocking.
win.nodelay(1)

# create the matrix to hold the tile values using NUMPY library
tilePool = []
tilePoolCount = []

for i in range(0,11):
    for j in range(0,11):
#        print '*********', i, '*', j, '=', i*j 
        if i*j not in tilePool:
            tilePool.append(i*j)
            tilePoolCount.append(1)
        else:
            tilePoolCount[tilePool.index(i*j)]+=1
# TODO adjust tileMatrix to hold valid values only. 
tileMatrix = numpy.random.random_integers(100,size=(4,4))
for i in range(0,4):
    for j in range(0,4):
        tileMatrix[i][j]=tilePool[numpy.random.random_integers(42,size=(1))]
# create the matrix to hold the matched tile values
matchedTileMatrix = numpy.zeros((4,4), int) 
# assigning a value to KEY_RIGHT
key = KEY_RIGHT

win.addstr( 4, 5, str(tileMatrix[0][0]))
win.addstr( 4, 9, str(tileMatrix[0][1]))
win.addstr( 4,13, str(tileMatrix[0][2]))
win.addstr( 4,17, str(tileMatrix[0][3]))
win.addstr( 5, 5, str(tileMatrix[1][0]))
win.addstr( 5, 9, str(tileMatrix[1][1]))
win.addstr( 5,13, str(tileMatrix[1][2]))
win.addstr( 5,17, str(tileMatrix[1][3]))
win.addstr( 6, 5, str(tileMatrix[2][0]))
win.addstr( 6, 9, str(tileMatrix[2][1]))
win.addstr( 6,13, str(tileMatrix[2][2]))
win.addstr( 6,17, str(tileMatrix[2][3]))
win.addstr( 7, 5, str(tileMatrix[3][0]))
win.addstr( 7, 9, str(tileMatrix[3][1]))
win.addstr( 7,13, str(tileMatrix[3][2]))
win.addstr( 7,17, str(tileMatrix[3][3]))


# MAIN WHILE LOOP START
# while the ESC key is not pressed, do the following
while key != 27:
# print the windows border
    win.border(0)
# TODO display the matrix that holds the tile values
# TODO highlight tile values as soon as they are matched
# print the two 12 faced dice values:
    xx = randint(0,10)
    yy = randint(0,10)
    win.addstr(1,  1, ' Die #1 * #2 = Total')
    win.addstr(2,  1, '     xx * yy = xyz  ')
    win.addstr(2,  1, '                             ')
    win.addstr(2,  1, '     ' + str(xx))
    win.addstr(2,  8, ' * '   + str(yy))
    win.addstr(2, 13, ' = '   + str(xx*yy)+'  ')
#    win.addstr(4,  3, ' 111 222 333 444 ')
#    win.addstr(5,  3, ' 111 222 333 444 ')
#    win.addstr(6,  3, ' 111 222 333 444 ')
#    win.addstr(7,  3, ' 111 222 333 444 ')
    ''' 
    win.addstr(0, 27, ' SNAKE ')                                   # 'SNAKE' strings
    win.addstr(1, 27, ' SNAKE ',curses.A_BLINK)                                   # 'SNAKE' strings
    win.addstr(2, 27, ' SNAKE ',curses.A_BOLD)                                   # 'SNAKE' strings
    win.addstr(3, 27, ' SNAKE ',curses.A_DIM)                                   # 'SNAKE' strings
    win.addstr(4, 27, ' SNAKE ',curses.A_REVERSE)                                   # 'SNAKE' strings
    win.addstr(5, 27, ' SNAKE ',curses.A_STANDOUT)                                   # 'SNAKE' strings
    win.addstr(6, 27, ' SNAKE ',curses.A_UNDERLINE)                                   # 'SNAKE' strings
    #win.addstr(7, 27, ' SNAKE ',)                                   # 'SNAKE' strings
    #win.addstr(8, 27, ' SNAKE ',)                                   # 'SNAKE' strings
    #win.refresh()
    '''
    
    win.addstr(2, 27, '        ')
    win.addstr(2, 27, str(numpy.argwhere(tileMatrix == xx*yy)))
    if str(len(numpy.argwhere(tileMatrix == xx*yy)))==1:
        win.addstr(3, 27, '  ')
        win.addstr(3, 27, str(numpy.argwhere(tileMatrix == xx*yy)[1]))
    else:
        win.addstr(3, 27, '  ')
 
    win.addstr(4, 27, str(len(numpy.argwhere(tileMatrix == xx*yy))))
    
    win.timeout(1000) 
    prevKey = key                                                  # Previous key pressed
    event = win.getch()
    key = key if event == -1 else event 


    if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
        key = -1                                                   # one (Pause/Resume)
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
        key = prevKey


# MAIN WHILE LOOP END    
curses.endwin()
