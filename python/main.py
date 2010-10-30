#!/usr/bin/env python
"""An example python application.

%prog [<some options>] <some arguments>

This script docstring serves as a usage message (with -h).

Kudos: http://www.artima.com/weblogs/viewpost.jsp?thread=4829

Modifed to use argparse (new in 2.7) instead of getopt.
"""
import sys
import argparse

def process(arg):
    """Print the given argument"""
    print "Argument: {}".format(arg)
    if arg == "error":
        return True
    return False

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv
    parser = argparse.ArgumentParser(
        description=__doc__, # printed with -h/--help
        # Don't mess woth formation of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument("-q", "--quiet", action="store_true", dest="quiet",
                        help="run quietly", default=False)
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument('args', metavar='args', type=str, nargs='+',
                        help='some extra arguments')
    args = parser.parse_args()
    if args.quiet:
        print "Running quietly..."
    # process arguments.
    for arg in args.args:
        error = process(arg) # process() is defined elsewhere
        if error:
            # Example of using error() method, which exits
            parser.error("Bad argument \"{}\"".format(arg))
    # Rest of main() function follows...

if __name__ == "__main__":
    sys.exit(main())
