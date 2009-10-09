#!/usr/bin/env python
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
    for line in ls:
	print len(line)
	win2.addstr(line)
	win2.refresh()
    stdscr.getch()

curses.wrapper(main)
