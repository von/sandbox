#!/usr/bin/env python
"""Demonstrate use of imp.load_source()"""

import argparse
import imp
import sys

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    mod = imp.load_source("imp.demo", "./imp-load-source-obj.py")
    c = mod.MyClass()
    c.doit()

if __name__ == "__main__":
    sys.exit(main())
