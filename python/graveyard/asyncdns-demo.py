#!/usr/bin/env python
"""Demo simple asycndns query

pip install asyncdns
"""

import argparse
import asyncdns
import logging
import sys
import time

class AsyncDNSQuery:
    resolver = asyncdns.Resolver()

    def __init__(self, qname):
        self.resolver.lookupAddress(qname, callback=self.callback)
        self.completed = False

    def callback(self, nameserver, qname, response):
        """Print the given argument"""
        nameserver_addr, nameserver_port = nameserver
        print "Got response from %s for %s: %s" % (nameserver_addr,
                                                   qname,
                                                   ",".join(response["A"]))
        self.completed = True

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
        description=__doc__, # printed with -h/--help
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
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument('hosts', metavar='args', type=str, nargs='+',
                        help='Hosts to look up')
    args = parser.parse_args()
    output_handler.setLevel(args.output_level)

    output.info("Processing arguments...")
    queries = []
    for host in args.hosts:
        output.debug("Querying for '{0}'...".format(host))
        queries.append(AsyncDNSQuery(host))
    while True:
        time.sleep(1)
        done = all([q.completed for q in queries])
        if done:
            break
    return(0)

if __name__ == "__main__":
    sys.exit(main())
