import glob
import curses
import time
from curses import wrapper

length = 30
width = 10

def init():
    stdscr = curses.initscr()
    curses.noecho()    # don't echo the keys on the screen
    curses.cbreak()    # don't wait enter for input
    stdscr.keypad(True)
    window = curses.newwin(length, width, 0, 0)  # create a 30x10 window
    window.box()       # Draw the box outside the window
    stdscr.clear()
    return window, stdscr

def destruct(window, stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def parseFile(cur_file):
    result = []
    for line in cur_file:
        result.append(line)
    return result

def main(stdscr):
    window, stdscr = init()

    frames = []
    filenames = glob.glob("2017/*.txt")
    for filename in filenames:
        cur_file = open(filename, "r")
        frames.append(parseFile(cur_file))

    for row in range(len(frames)):
        for col in range(len(frames[row])):
            stdscr.addstr(row, col, (frames[row][col]))
            stdscr.refresh()
        time.sleep(0.2)

    destruct(window, stdscr)

wrapper(main)
# if __name__ == "__main__":
#     main()
