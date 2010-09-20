#!/usr/bin/env python
"""An example python application.

%prog [<some options>] <some arguments>

This script docstring serves as a usage message (with -h).

Kudos: http://www.artima.com/weblogs/viewpost.jsp?thread=4829

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
        usage=__doc__, # printed with -h/--help
        version="%prog 1.0" # automatically generates --version
        )
    parser.add_option("-q", "--quiet", action="store_true", dest="quiet",
                      help="run quietly", default=False)
    (options, args) = parser.parse_args()
    if options.quiet:
        print "Running quietly..."
    # process arguments.
    for arg in args:
        error = process(arg) # process() is defined elsewhere
        if error:
            # Example of using error() method, which exits
            parser.error("Bad argument %s" % arg)
    # Rest of main() function follows...

if __name__ == "__main__":
    sys.exit(main())
