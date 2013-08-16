#!/usr/bin/env python
"""An example python application.

Kudos: http://www.artima.com/weblogs/viewpost.jsp?thread=4829

Modified to use docopt (pip install docopt)

Usage: docopt_demo.py [options] [<arg>...]

Options:
      -h, --help   show this help message and exit
      -d, --debug  Turn on debugging
      -q, --quiet  run quietly
      --version    show program's version number and exit
"""
from __future__ import print_function  # So we can get at print()

import argparse
import sys

from docopt import docopt  # pip install docopt

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
        argv = sys.argv[1:]

    # If version is missing, then --version will cause error exit.
    args = docopt(__doc__, argv=argv, version="0.1")

    global output
    output = print if not args['--quiet'] else lambda s: None
    global debug
    debug = print if args['--debug'] else lambda s: None

    output("Processing arguments...")
    for arg in args['<arg>']:
        debug("Processing '{}'...".format(arg))
        error = process(arg)
        if error:
            # Example of using error() method, which exits
            parser.error("Bad argument \"{}\"".format(arg))
    output("Rest of main() would normally run here...")
    return(0)

if __name__ == "__main__":
    sys.exit(main())
