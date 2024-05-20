import curses
from curses import wrapper
text = "The brown fox jumped over the fence. The King of Britain is currently sick.\nIn the Bible there was a king named Xerxes and Ahaseurus. They both died colloquially.  "


def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello World")
    stdscr.refresh()
    stdscr.getKey()

wrapper(main)