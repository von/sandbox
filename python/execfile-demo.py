#!/usr/bin/env python
"""Demonstration of execfile() and namespaces"""

import sys

if __name__ == "__main__":
    print "Executing myself..."
    globals = {"hello_world":"Hello World!"}
    execfile(sys.argv[0], globals)
    print globals["hello_world"]

elif __name__ == "__builtin__":
    print "Being executed..."
    print hello_world
    hello_world = "Goodbye"
