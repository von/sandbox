#!/usr/bin/env python
"""Demonstrate use of profile and runctx() in particular.

See http://docs.python.org/library/profile.html

Kudos to following for runctx():
"""
import cProfile

import sys
from optparse import OptionParser

class profileTester:
    def DoIt(self):
        sum = 0
        for i in range(1000):
            sum += 1

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
    p = profileTester()

    # cProfile.run() will just use __main__ context instead of the calling
    # frame, so since we are instead a function, we need to give it our
    # context, which we can do with the runctx() method.
    #
    # Kudos: http://www.velocityreviews.com/forums/t677326-profiler-throws-nameerror-on-any-function.html
    cProfile.runctx("p.DoIt()", globals(), locals())

if __name__ == "__main__":
    sys.exit(main())
