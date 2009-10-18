#!/usr/bin/env python
"""Module docstring.

This serves as a long usage message.

This is an example python application. Kudos:
http://www.artima.com/weblogs/viewpost.jsp?thread=4829

Modifed to use optparse instead of getopt.
"""
import sys
from optparse import OptionParser

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv
    parser = OptionParser(
        usage="%prog [<options>] <some arg>", # printed with -h/--help
        version="%prog 1.0" # automatically generates --version
        )
    parser.add_option("-q", "--quiet", action="store_true", dest="quiet",
                      help="run quietly", default=False)
    (options, args) = parser.parse_args()
    if options.quiet:
        print "Running quietly..."
    # process arguments.
    for arg in args:
        process(arg) # process() is defined elsewhere
    # Rest of main() function follows...

if __name__ == "__main__":
    sys.exit(main())
