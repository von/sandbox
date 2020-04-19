#!/usr/bin/env python
"""Demo of Python3's new print() function.

Kudos: David Beazley's Mastering Python3 I/O
"""
# Needed for Python2
from __future__ import print_function

import argparse
import logging
import sys

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    # Set up out output via logging module
    output = logging.getLogger(argv[0])
    output.setLevel(logging.DEBUG)
    output_handler = logging.StreamHandler(sys.stdout)
    # Set up formatter to just print message without preamble
    output_handler.setFormatter(logging.Formatter("%(message)s"))
    output.addHandler(output_handler)

    # Argument parsing
    parser = argparse.ArgumentParser(
        description=__doc__, # printed with -h/--help
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    # Only allow one of debug/quiet mode
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("-d", "--debug",
                                 action='store_const', const=logging.DEBUG,
                                 dest="output_level", default=logging.INFO,
                                 help="print debugging")
    verbosity_group.add_argument("-q", "--quiet",
                                 action="store_const", const=logging.WARNING,
                                 dest="output_level",
                                 help="run quietly")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument('args', metavar='args', type=str, nargs='*',
                        help='some extra arguments')
    args = parser.parse_args()
    output_handler.setLevel(args.output_level)
    argv = args.args
    if not argv:
        output.warning("This demo works better if you "
                       "supply some commandline arguments. ")
    output.info("Simple print of all arguments...")
    print(*argv)
    output.info("Print of all arguments with sep=':'")
    print(*argv, sep=':')
    output.info("Print of all arguments with end=' -END-\\n'")
    print(*argv, end=' -END-\n')
    output.info("Print of all arguments with file=sys.stderr")
    print("Stderr:", *argv, file=sys.stderr)
    return(0)

if __name__ == "__main__":
    sys.exit(main())
