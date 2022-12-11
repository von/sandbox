#!/usr/bin/env python3
"""Demonstrate PEP 572 assignment expressions"""
# Kudos: https://stackoverflow.com/a/55882141/197789

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

sys.exit(0)
