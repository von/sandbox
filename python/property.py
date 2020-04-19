#!/usr/bin/env python3
"""
Demonstrate use of property()

Kudos:
http://adam.gomaa.us/blog/2008/aug/11/the-python-property-builtin/
"""
from pydoc import help
import sys

class Foo:
    """Property test"""

    def __init__(self, value):
        self.value = value

    @property
    def value2(self):
        return self.value*2

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def delValue(self):
        del(self.value)

    # Define everything at once
    value3 = property(getValue, setValue, delValue, "value3 doc string")

def main():
    f = Foo(4)
    assert(f.value2 == 8)
    # In Python2 the following works, but in Python3 it raises
    # an AttributeError
    try:
        f.value2 = 5     # This will override value2() method
    except AttributeError:
        assert(f.value2 == 8)
    else:
        assert(f.value2 == 5)
    assert(f.value3 == 4)
    f.value3 = 6
    assert(f.value3 == 6)
    del(f.value3)
    print("Success.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
