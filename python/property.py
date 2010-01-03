#!/usr/bin/env python
"""
Demonstrate use of property()

Kudos:
http://adam.gomaa.us/blog/2008/aug/11/the-python-property-builtin/
"""
import sys

class Foo:
    def __init__(self, value):
        self.value = value

    @property
    def value2(self):
        return self.value*2

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    # Define everything at once
    value3 = property(getValue, setValue)

def main():
    f = Foo(4)
    assert(f.value2 == 8)
    f.value2 = 5     # This will override value2() method
    assert(f.value2 == 5)
    assert(f.value3 == 4)
    f.value3 = 6
    assert(f.value3 == 6)
    print "Success."
    return 0

if __name__ == "__main__":
    sys.exit(main())
