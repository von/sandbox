#!/usr/bin/env python3
"""Show how to call method based on a string mapping

See decorated-mapped-methods.py for a way to do this with decorators"""

class A:
    def __init__(self, value):
        self.MAPPINGS[value](self)

    def foo(self):
        print("foo")

    def bar(self):
        print("bar")

    def foobar(self):
        print("foobar")

    MAPPINGS = {
        1 : foo,
        2 : bar,
        3 : foobar,
        }

A(1)
A(2)
A(3)
