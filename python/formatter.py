#!/usr/bin/env python3
"""Demonstrate overriding of Formatter""" 

import argparse
import string
import sys

class MyObj:
    def __str__(self):
        return "Hello world!"

class MyFormatter(string.Formatter):
    """Formatter subclass that intercepts certain values and returns
    an object instead of value from kwargs."""
    intercepts = {
        "foo" : MyObj,
        }

    def get_value(self, key, args, kwargs):
        if key in self.intercepts:
            return self.intercepts[key]()
        return string.Formatter.get_value(self, key, args, kwargs)

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    f = MyFormatter()
    print(f.format("This {var} a {foo} test {1}", "real", "world", var="IS"))
    return(0)

if __name__ == "__main__":
    sys.exit(main())
