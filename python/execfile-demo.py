#!/usr/bin/env python3
"""Demonstration of execfile() and namespaces"""

import sys

if __name__ == "__main__":
    print("Executing myself...")
    globals = {"hello_world":"Hello World!"}
    exec(compile(open(sys.argv[0], "rb").read(), sys.argv[0], 'exec'), globals)
    print(globals["hello_world"])

# In Python3, this was "__builtins__"
# Kudos: https://stackoverflow.com/a/11181616/197789
elif __name__ == "builtins":
    print("Being executed...")
    print(hello_world)
    hello_world = "Goodbye"
