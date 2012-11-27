#!/usr/bin/env python
"""An example of the cmd module"""
import argparse
import cmd
import shlex
import subprocess
import sys

class MyCmd(cmd.Cmd):
    prompt = "MyCmd> "

    def default(self, line):
        """Called for unrecognizted command."""
        print "Unrecognized: " + line

    def do_EOF(self, remainder):
        """Handle EOF"""
        self.do_quit(remainder)

    def do_echo(self, remainder):
        """Echo arguments"""
        print remainder

    def do_ls(self, remainder):
        """List files"""
        retcode = subprocess.call(['ls'] + self._split(remainder))

    def do_quit(self, remainder):
        """Quit"""
        sys.exit(0)

    def do_split(self, remainder):
        """Split and echo arguments"""
        args = self._split(remainder)
        print ",".join(args)

    @staticmethod
    def _split(line):
        """Split line into tokens handling quoted substrings"""
        return shlex.split(line)

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

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
                                 action='store_true', default=False,
                                 help="Turn on debugging")
    verbosity_group.add_argument("-q", "--quiet",
                                 action="store_true", default=False,
                                 help="run quietly")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument('args', metavar='args', type=str, nargs='*',
                        help='some extra arguments' +\
                            ' (use "error" to trigger an error)')
    args = parser.parse_args()

    my_cmd = MyCmd()
    my_cmd.cmdloop()

    return(0)

if __name__ == "__main__":
    sys.exit(main())
