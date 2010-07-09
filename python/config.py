#!/usr/bin/env python
"""ConfigParser.py

Demonstrate ConfigParser module
"""
from ConfigParser import SafeConfigParser
import sys
from optparse import OptionParser

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv
    parser = OptionParser(
        usage="%prog [<options>]", # printed with -h/--help
        version="%prog 1.0" # automatically generates --version
        )
    parser.add_option("-c", "--configfile", action="store", dest="confpath",
                      help="specific configuration file path")
    parser.set_defaults(confpath="config.conf")
    (options, args) = parser.parse_args()

    print "Reading %s" % options.confpath
    config = SafeConfigParser()
    config.read(options.confpath)
    for section in config.sections():
        print "[%s]" % section
        for option in config.options(section):
            print option

if __name__ == "__main__":
    sys.exit(main())
