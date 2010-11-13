#!/usr/bin/env python
"""coroutine demonstration

Kudos: David Beazley http://www.dabeaz.com/coroutines/

A coroutine uses (yield) as defined by PEP-342. (yield) routine waits for
a value to be passed to the coroutine by its send() method.

Note that despite the fact coroutines and generators both use yield, don't
confuse or mix them.
"""
import sys

def coroutine(func):
    """Function decorator priming a coroutine by calling next() once automatically"""
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

def generator_function(n):
    """Return string representations of number 1..n"""
    for i in range(n):
        yield str(i)

class generator_class(object):
    def __init__(self, max):
        self.count = 0
        self.max = max

    def __iter__(self):
        """Called when instance appears in the for look. If you create an
        instance first you can pass a value to __iter__(), e.g.:

        gc = generator_class(10)
        for i in gc(5):  # <- This requires __iter__ to accept a 2nd argument.
            do_something(i)

        If you use the class in the for line, __iter__ is called with no
        arguments, e.g.:

        # 10 gets passed to __init__()
        # __iter__() just gets self
        for i in generator_class(10): 
            do_something(i)
        """
        return self

    def next(self):
        self.count += 1
        if self.count > self.max:
            raise StopIteration
        else:
            return str(self.count)

@coroutine
def grep(pattern, target):
    """A coroutine that looks for pattern in its input (which must be a string)
    and passes it to coroutine target if it finds it."""
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)

@coroutine
def printer(prefix):
    """A coroutine that prints its input with the given prefix."""
    while True:
        line = (yield)
        print prefix, line.rstrip()

def send_generator_to_coroutine(generator, target):
    """Send output from the given generator to the given coroutine.

    Note this function is not a coroutine, it just feeds one."""
    for item in generator:
        target.send(item)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    print "Sending my source code to grep('while') and then printer()..."
    # Take one with file as generator
    with file(argv[0]) as f:
        g = send_generator_to_coroutine(f, grep("while", printer("My output:")))
    # Take two, building pipe slowly and using generator function
    p = printer("Second output:")
    g = grep("5", p)
    gf = generator_function(10)
    send_generator_to_coroutine(gf, g)
    # Take three, with generator_class
    p = printer("Third output:")
    g = grep("7", p)
    gc = generator_class(11)
    send_generator_to_coroutine(gc, g)

    print "Done."

if __name__ == "__main__":
    sys.exit(main())
