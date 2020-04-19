#!/usr/bin/env python3
"""Demonstrate singleton in python.

Kudos: http://code.activestate.com/recipes/66531/#c22

TODO: Thread safety, add lock to __new__()

Note good point in http://code.activestate.com/recipes/66531/#c23 that
modules and classes are already singletons in python.
"""

class Singleton(object):
    def __new__(cls, *p, **k):
        if not '_the_instance' in cls.__dict__:
            cls._the_instance = object.__new__(cls, *p, **k)
        return cls._the_instance

a = Singleton()
b = Singleton()
print(a)
print(b)
print(a==b)
