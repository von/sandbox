#!/usr/bin/env python3
"""Demonstrate use of new Python 3.6+ f-strings

https://www.python.org/dev/peps/pep-0498/
"""

print("A python f-string renames parameters with coorsponding variable names.")
name="world"
print(f"Hello {name}!")

print("They can also include expressions:")
a=5
b=10
print(f"{a} + {b} = {a + b}")
