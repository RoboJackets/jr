import glob
import curses
import time
from curses import wrapper

length = 30
width = 10

def init():
    curses.noecho()    # don't echo the keys on the screen
    curses.cbreak()    # don't wait enter for input
    window = curses.newwin(length, width, 0, 0)  # create a 30x10 window
    window.box()       # Draw the box outside the window
    return window

def destruct(window, stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def parseFile(cur_file):
    result = []



def main(stdscr):
    window = init()

    frame = []
    filenames = glob.glob("art/*.txt")
    for filename in filenames:
        cur_file = open(filename, "r")
        frame.append(parseFile(cur_file))

    for row in range(len(frame)):
        for col in range(len(frame[row])):
            stdscr.addch(row, col, frame[row][col])
            stdscr.refresh()
        time.sleep(0.2)

    destruct(window, stdscr)

wrapper(main)
