#!/usr/bin/env python3
"""Simple demonstration of class variables

%prog
"""
import sys
from optparse import OptionParser

class Class():
    var1 = 1
    var2 = 5

    def increment_var1(self):
        """This won't work as a class variable it causes an instance variable to be created"""
        self.var1 += 1
        return self.var1

    def increment_var2(self):
        """This will work as a class variable"""
        Class.var2 += 1
        return Class.var2

def main(argv=None):
    if argv is None:
        argv = sys.argv
    parser = OptionParser(
        usage=__doc__, # printed with -h/--help
        version="%prog 1.0" # automatically generates --version
        )
    parser.add_option("-q", "--quiet", action="store_true", dest="quiet",
                      help="run quietly", default=False)
    (options, args) = parser.parse_args()
    c = Class()
    c2 = Class()
    print("These will be the same:")
    print(c.increment_var1())
    print(c2.increment_var1())
    print("These will be different:")
    print(c.increment_var2())
    print(c2.increment_var2())

if __name__ == "__main__":
    sys.exit(main())
