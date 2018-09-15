import glob
import curses
import time
from curses import wrapper

width = 80
height = 30

def init():
    stdscr = curses.initscr()

    term_height,term_width = stdscr.getmaxyx()

    curses.noecho()    # don't echo the keys on the screen
    curses.cbreak()    # don't wait enter for input
    window = curses.newwin(width, height, 0, 0)  # create a window
    if term_height <= height or term_width <= width:
        destruct(stdscr, window)
        print "\x1b[8;" + str(height + 1) + ";" + str(width + 1) + "t"
        time.sleep(1)
        stdscr, window = init()
        #quit()

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
        if len(line) < width:
            line += " " * (width - len(line))
        result.append(line)
    if len(result) < height:
        for i in range(height - len(result)):
            result.append(" " * width)
    return result

def main(stdscr):
    print "temp"
    window, stdscr = init()

    frames = []
    black = []
    for i in range(height):
        black.append(" " * width)
    frames.append(black)
    frames.append(parseFile(open("required/ship.txt", "r")))
    for yearFolder in glob.glob("years/*"):
        for folder in glob.glob(yearFolder+"/*")[::-1]:
            for filename in glob.glob(folder+"/*.txt"):
                cur_file = open(filename, "r")
                frames.append(parseFile(cur_file))
    frames.append(parseFile(open("required/jason.txt", "r")))
    emptyFile = [[" "] * width] * height
    frames.append(emptyFile)
    for start_col in range((len(frames) - 1) * width):
        for col in range(width):
            for row in range(height):
                stdscr.addch(row, col, (frames[(start_col + col) / width][row][(start_col + col) % width]))
        stdscr.refresh()
        time.sleep(0.05)
    destruct(window, stdscr)

if __name__ == "__main__":
    wrapper(main)
