#!/usr/bin/env python
import sys

class Foo:
    def __init__(self, value):
        self.value = value

    @property
    def value2(self):
        return self.value*2

def main():
    f = Foo(4)
    print f.value2

if __name__ == "__main__":
    sys.exit(main())
