#!/usr/bin/env python
"""Examples of decorators"""

class MyDecorator1(object):
    """Example of decorator using a class and __call__()

    Kudos: http://www.artima.com/weblogs/viewpost.jsp?thread=240808
    """
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print "Calling decorated function {0.__name__}".format(self.function)
        self.function(*args, **kwargs)
        print "Exiting decorated function {0.__name__}".format(self.function)

def MyDecorator2(function):
    """Exacmple of decorator using a function"""
    def new_function(*args, **kwargs):
        print "Calling decorated function {0.__name__}".format(function)
        function(*args, **kwargs)
        print "Exiting decorated function {0.__name__}".format(function)
    return new_function

@MyDecorator1
def func1(msg):
    print "Inside func1({})".format(msg)

@MyDecorator2
def func2(msg):
    print "Inside func2({})".format(msg)

func1("Hello world")
func2("Goodbye world")

