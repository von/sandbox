#!/usr/bin/env python
"""An example python application.

This script docstring serves as a usage message (with -h).

Kudos: http://www.artima.com/weblogs/viewpost.jsp?thread=4829

Modified to use argparse (new in 2.7) instead of getopt.
"""
from __future__ import print_function  # So we can get at print()

import argparse
import pdb
import sys
import traceback


# Handle uncaught exception by opening debugger
# Kudos: Doug Hellman and http://stackoverflow.com/a/6234491/197789
def exception_catcher(type, value, tb):
    """Handle uncaught exceptions

    Intended to be used for sys.excepthook"""
    traceback.print_exc()
    pdb.post_mortem(tb)

sys.excepthook = exception_catcher


# Output functions
output = print
debug = print

def process(arg):
    """Print the given argument"""
    output("Argument: {}".format(arg))
    # Allow command-line argument to create an error
    if arg == "error":
        return True
    return False

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    # Argument parsing
    parser = argparse.ArgumentParser(
        description=__doc__, # printed with -h/--help
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # To have --help print defaults with trade-off it changes
        # formatting, use: ArgumentDefaultsHelpFormatter
        )
    # Only allow one of debug/quiet mode
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("-d", "--debug",
                                 action='store_true', default=False,
                                 help="Turn on debugging")
    verbosity_group.add_argument("-q", "--quiet",
                                 action="store_true", default=False,
                                 help="run quietly")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument('args', metavar='args', type=str, nargs='+',
                        help='some extra arguments' +\
                            ' (use "error" to trigger an error)')
    args = parser.parse_args()

    global output
    output = print if not args.quiet else lambda s: None
    global debug
    debug = print if args.debug else lambda s: None

    output("Processing arguments...")
    for arg in args.args:
        debug("Processing '{}'...".format(arg))
        error = process(arg)
        if error:
            # Example of using error() method, which exits
            parser.error("Bad argument \"{}\"".format(arg))
    output("Rest of main() would normally run here...")
    return(0)

if __name__ == "__main__":
    sys.exit(main())
