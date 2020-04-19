#!/usr/bin/env python3
"""An example python application.

This script docstring serves as a usage message (with -h).

Kudos: http://www.artima.com/weblogs/viewpost.jsp?thread=4829

Modified to use argparse (new in 2.7) instead of getopt.
Modified to using logging for output.
"""
import argparse
import logging
import sys


def process(arg):
    """Print the given argument"""
    print("Argument: {arg}")
    # Allow command-line argument to create an error
    if arg == "error":
        return True
    return False


def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    # Set up out output via logging module
    output = logging.getLogger(argv[0])
    output.setLevel(logging.DEBUG)
    output_handler = logging.StreamHandler(sys.stdout)  # Default is sys.stderr
    # Set up formatter to just print message without preamble
    output_handler.setFormatter(logging.Formatter("%(message)s"))
    output.addHandler(output_handler)

    # Argument parsing
    parser = argparse.ArgumentParser(
        description=__doc__,  # printed with -h/--help
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # To have --help print defaults with trade-off it changes
        # formatting, use: ArgumentDefaultsHelpFormatter
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
    parser.add_argument("-f", "--log_file",
                        help="Log output to file", metavar="FILE")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument('args', metavar='args', type=str, nargs='+',
                        help='some extra arguments' +
                        ' (use "error" to trigger an error)')
    args = parser.parse_args()
    output_handler.setLevel(args.output_level)
    if args.log_file:
        file_handler = logging.FileHandler(args.log_file)
        file_handler.setFormatter(logging.Formatter("%(asctime)s:%(message)s"))
        output.addHandler(file_handler)
        output.debug("Logging to file {}".format(args.log_file))
    output.info("Processing arguments...")
    for arg in args.args:
        output.debug("Processing '{}'...".format(arg))
        error = process(arg)
        if error:
            # Example of using error() method, which exits
            parser.error("Bad argument \"{}\"".format(arg))
    output.warning("Rest of main() would normally run here...")
    return(0)

if __name__ == "__main__":
    sys.exit(main())
