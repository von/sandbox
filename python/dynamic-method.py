#!/usr/bin/env python3
"""Demonstrate creation of a dynamic method on an instance

Kudos: https://stackoverflow.com/a/37455782/197789
"""
import sys
import textwrap
import types


class DynMethod:

    def __init__(self, code_string):
        """Create an instance with a method f() implementing code_string

        code_string should be one or more lines of python code processing
        arg and returning a result."""
        code = "def f(self, arg):\n"
        # Following requires >= Python 3.3
        code += textwrap.indent(code_string, "    ")
        globals = {}
        exec(code, globals)  # Create f() in globals
        # Add f() as a method to self
        self.f = types.MethodType(globals["f"], self)


f1 = "return arg * 2"
d1 = DynMethod(f1)
print(f"{f1}: 10 -> {d1.f(10)}")

f2 = "return arg * 2 + 8"
d2 = DynMethod(f2)
print(f"{f2}: 10 -> {d2.f(10)}")

f3 = "return arg > 5"
d3 = DynMethod(f3)
print(f"{f3}: 10 -> {d3.f(10)}")

sys.exit(0)
