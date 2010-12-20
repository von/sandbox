#!/usr/bin/env python
"""Demonstration script for PackageDemo."""
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
    output_handler = logging.StreamHandler(sys.stdout)  # Default is sys.stderr
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

    args = parser.parse_args()
    output_handler.setLevel(args.output_level)

    output.info("Importing PackageDemo.FooClass")
    from PackageDemo import FooClass
    print FooClass.__doc__
    foo = FooClass

    output.info("Importing PackageDemo.SomeClass")
    from PackageDemo import SomeClass
    print SomeClass.__doc__
    some = SomeClass

    output.info("Getting package path")
    from PackageDemo import my_package_path
    print "Package path is:", my_package_path
                
    output.info("That's all")
    return(0)

if __name__ == "__main__":
    sys.exit(main())
