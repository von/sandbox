#!/usr/bin/env python3
import curses
import os

def main(stdscr):
    win1 = curses.newwin(3, 30, 2,0)
    win1.border()
    win2 = curses.newwin(10, 30, 10,0)
    win2.border()
    stdscr.addstr(0,0, "Testing...")
    win1.addstr(0,0, "Foobar")
    win2.addstr(0,0, "I win")
    stdscr.refresh()
    win1.refresh()
    win2.refresh()
    stdscr.getch()
    win2.clear()
    win2.addstr(0,0, "2..3..")
    win2.refresh()
    stdscr.getch()
    ls = os.popen("ls")
    for i,line in enumerate(ls):
        try:
            win2.addstr(i, 0, line.encode("utf-8"))
        except curses.error:
            # Assume we've hit the end of the window
            break
    win2.refresh()
    stdscr.getch()

curses.wrapper(main)
