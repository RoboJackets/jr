import glob
import curses
import time
from curses import wrapper

length = 80
width = 30

def init():
    stdscr = curses.initscr()
    curses.noecho()    # don't echo the keys on the screen
    curses.cbreak()    # don't wait enter for input
    stdscr.keypad(True)
    window = curses.newwin(length, width, 0, 0)  # create a window
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
        if len(line) < length:
            line += " " * (length - len(line))
        result.append(line)
    if len(result) < width:
        for i in range(width - len(result)):
            result.append(" " * length)
    return result

def main(stdscr):
    window, stdscr = init()

    frames = []
    black = []
    for i in range(width):
        black.append(" " * length)
    frames.append(black)
    frames.append(parseFile(open("required/ship.txt", "r")))
    for filename in glob.glob("Instructors/*.txt"):
        cur_file = open(filename, "r")
        frames.append(parseFile(cur_file))
    for filename in glob.glob("2017/*.txt"):
        cur_file = open(filename, "r")
        frames.append(parseFile(cur_file))
    frames.append(parseFile(open("required/jason.txt", "r")))
    for start_col in range((len(frames) - 1) * length):
        for col in range(length):
            for row in range(width):
                stdscr.addch(row, col, (frames[(start_col + col) / length][row][(start_col + col) % length]))
        stdscr.refresh()
        time.sleep(0.05)
    destruct(window, stdscr)

if __name__ == "__main__":
    wrapper(main)
