#!/usr/bin/env python3
"""Example of conditional expression as defined by PEP 308

following pythong syntax:

>>> foo = 1 if bar else 2
"""

bar = True

foo = 1 if bar else 2

print(f"foo = {foo}")

bar = False

foo = 1 if bar else 2

print(f"foo = {foo}")

