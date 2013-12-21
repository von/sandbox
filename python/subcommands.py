#!/usr/bin/env python
"""An example of subcommands with argparse """
from __future__ import print_function  # So we can get at print()

import argparse
import sys

# Output functions
output = print


def foo(args):
    """Do a foo thing"""
    output("Foo!")
    return 0


def bar(args):
    """Do a bar thing"""
    output("Bar!")
    return 0


def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    # Argument parsing
    parser = argparse.ArgumentParser(
        description=__doc__,  # printed with -h/--help
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # To have --help print defaults with trade-off it changes
        # formatting, use: ArgumentDefaultsHelpFormatter
    )
    subparsers = parser.add_subparsers(help='sub-command help')

    # create the parser for the "foo" command
    parser_foo = subparsers.add_parser('foo', help=foo.__doc__)
    parser_foo.set_defaults(func=foo)

    # create the parser for the "bar" command
    parser_bar = subparsers.add_parser('bar', help=bar.__doc__)
    parser_bar.set_defaults(func=bar)

    args = parser.parse_args()

    func = args.func
    status = func(args)
    return status

if __name__ == "__main__":
    sys.exit(main())
