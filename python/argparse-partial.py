#!/usr/bin/env python
"""Demonstrate how to use argparse.parse_known_options()

In this case, we use it to allow a configuration file to specify default
for commandline options.

Default with no user input:

$ ./argparse-partial.py
No configuration file specified.
Option is default

Default from configuration file:

$ ./argparse-partial.py -c argparse-partial.config 
Configuration file is argparse-partial.config
Option from config is Hello world!
Option is Hello world!

Default from configuration file, overridden by commandline:

$ ./argparse-partial.py -c argparse-partial.config --option override
Configuration file is argparse-partial.config
Option from config is Hello world!
Option is override
"""
import argparse
import ConfigParser
import sys

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    # Parse any conf_file specification
    # We make this parser with add_help=False so that
    # it doesn't parse -h and print help.
    conf_parser = argparse.ArgumentParser(
        description=__doc__, # printed with -h/--help
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # Turn off help, so we print all options in response to -h
        add_help=False
        )
    conf_parser.add_argument("-c", "--conf_file",
                        help="Specify config file", metavar="FILE")
    args, remaining_argv = conf_parser.parse_known_args()
    defaults = {
        "option" : "default"
        }
    if args.conf_file:
        print "Configuration file is {}".format(args.conf_file)
        config = ConfigParser.SafeConfigParser()
        config.read([args.conf_file])
        if config.has_option("Defaults", "option"):
            value = config.get("Defaults", "option")
            print "Option from config is {}".format(value)
            defaults["option"] = value
    else:
        print "No configuration file specified."

    # Parse rest of arguments
    # Don't surpress add_help here so it will handle -h
    parser = argparse.ArgumentParser(
        # Inherit options from config_parser
        parents=[conf_parser]
        )
    parser.set_defaults(**defaults)
    parser.add_argument("--option")
    args = parser.parse_args(remaining_argv)
    print "Option is {}".format(args.option)
    return(0)

if __name__ == "__main__":
    sys.exit(main())
