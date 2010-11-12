#!/usr/bin/env python

def some_function(i):
    """Given an integer, add 5 to it.

    >>> some_function(5)
    10
    """
    return i+5

class some_class(object):
    """Get a class that generates integers.

    >>> c = some_class(7)
    >>> c.generate()
    7
    >>> # Testing for exceptions
    >>> c.some_old_method_now_gone()
    Traceback (most recent call last):
    ...
    AttributeError: 'some_class' object has no attribute 'some_old_method_now_gone'
    """

    def __init__(self, i):
        self.value = i

    def generate(self):
        return self.value
 
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)

