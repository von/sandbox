#!/usr/bin/env python
"""An example python application.

This allow for specification of a configuration file that can be
overridden by command line options.

This script docstring serves as a usage message (with -h).

Kudos: http://www.artima.com/weblogs/viewpost.jsp?thread=4829

Modified to use argparse (new in 2.7) instead of getopt.
Modified to using logging for output.
Modified to read configuration file for defaults.
"""
import argparse
import ConfigParser
import logging
import logging.config
import sys

def process(arg):
    """Print the given argument"""
    print "Argument: {}".format(arg)
    # Allow command-line argument to create an error
    if arg == "error":
        return True
    return False

def parse_args(argv):
    """Parse commandline arguments taking default from configuration file.

    If --conf_file is specified, it will be read and used to set defaults
    according to conf_mappings."""
    # Parse any conf_file specification
    # We make this parser with add_help=False so that
    # it doesn't parse -h and print help.
    conf_parser = argparse.ArgumentParser(
        # Turn off help, so we print all options in response to -h
        add_help=False
        )
    conf_parser.add_argument("-c", "--conf_file",
                        help="Specify config file", metavar="FILE")
    args, remaining_argv = conf_parser.parse_known_args(argv[1:])
    defaults = {
        "output_level" : logging.INFO,
        "option" : "default option",
        }
    if args.conf_file:
        # Mappings from configuraition file to options
        conf_mappings = [
            # ((section, option), option)
            (("Defaults", "option"), "option")
            ]
        config = ConfigParser.SafeConfigParser()
        config.read([args.conf_file])
        for sec_opt, option in conf_mappings:
            if config.has_option(*sec_opt):
                value = config.get(*sec_opt)
                defaults[option] = value

    # Parse rest of arguments
    # Don't surpress add_help here so it will handle -h
    parser = argparse.ArgumentParser(
        # Inherit options from config_parser
        parents=[conf_parser],
        # print script description with -h/--help
        description=__doc__,
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.set_defaults(**defaults)
    # Only allow one of these logging options
    logging_group = parser.add_mutually_exclusive_group()
    logging_group.add_argument("-d", "--debug",
                               action='store_const', const=logging.DEBUG,
                               dest="output_level", 
                               help="print debugging")
    logging_group.add_argument("-q", "--quiet",
                               action="store_const", const=logging.WARNING,
                               dest="output_level",
                               help="run quietly")
    logging_group.add_argument("-l", "--logging_config",
                               help="Read logging configuration from file",
                               metavar="FILE")
    parser.add_argument("--option", help="some option")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument('args', metavar='args', type=str, nargs='+',
                        help='some extra arguments' +\
                            ' (use "error" to trigger an error)')
    args = parser.parse_args(remaining_argv)
    return args

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    args = parse_args(argv)

    if args.logging_config:
        logging.config.fileConfig(args.logging_config)
        output = logging.getLogger(argv[0])
    else:
        # Set up out output via logging module
        output = logging.getLogger(argv[0])
        output.setLevel(logging.DEBUG)
        # Change from default sys.stderr
        output_handler = logging.StreamHandler(sys.stdout)
        # Set up formatter to just print message without preamble
        output_handler.setFormatter(logging.Formatter("%(message)s"))
        output.addHandler(output_handler)
        output_handler.setLevel(args.output_level)

    output.info("Option is \"{}\"".format(args.option))
    output.info("Processing arguments...")
    for arg in args.args:
        output.debug("Processing '{}'...".format(arg))
        error = process(arg)
        if error:
            output.error("Bad argument \"{}\"".format(arg))
            sys.exit(1)
    output.warning("Rest of main() would normally run here...")
    return(0)

if __name__ == "__main__":
    sys.exit(main())
