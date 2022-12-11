#!/usr/bin/env python3
"""Demonstrate PEP 572 assignment expressions"""
# Kudos: https://stackoverflow.com/a/55882141/197789

import re
import sys

a = 4
print(f"a = {a}")

# Should set a to False and evaluate as False
if a := False:
    print(f"a = {a} - should not get here!")

print(f"a = {a}")

# Should set a to 8 and evaluate as True
if a := 8:
    print(f"a = {a}")

# Demonstrate if/elif context
# Put in parens to force desired ordering. Otherwise "10 > 20" evaluates
# first and a will be set to False
if (a := 10) > 20:
    print(f"{a} > 20 - should not get here!")
elif a < 12:
    print(f"{a} < 12")
else:
    print(f"!{a} < 12 - should not get here!")

# Example with regexs
r1 = re.compile("abc*")
r2 = re.compile("def*")
line = "deffffffff!"

if m := r1.match(line):
    print(f"{line} matched r1 - should not get here!")
elif m := r2.match(line):
    print(f"{line} matched r2 as expected: {m.group(0)}")

sys.exit(0)
