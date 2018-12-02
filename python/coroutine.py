#!/usr/bin/env python
"""coroutine and generator demonstration

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

# Don't use '@coroutine' decorator here for demonstration purposes
def coroutine_example(starting_sum=0):
    """When invoked, a GeneratorType is returned.

    The first time next() (or send(None)) is invoked, everything up to the
    first yield is run (and the RValue of the yield is returned).

    On the first send() the argument to the send() call is returned from the
    yield and the function is run until the next yield. At which point
    the RValue to the yield is returned from the calling send().

    This example computes a running sum. This is a simple example of keeping
    state in a coroutine. Seems like the biggest win of coroutines over
    regular functions is state. More complex examples would be open files
    sockets, queues, etc.

    This whole yield RValue thing I got from:
    http://dabeaz.blogspot.com/2010/07/yieldable-threads-part-1.html
    Is also in coroutines tutorial starting around slide 135.
    """
    sum = starting_sum
    while True:
        value = yield sum
        sum += value

def coroutine_example2(starting_sum=0):
    """Another exmple with yield split into two yields, but otherwise
    the same."""
    sum = starting_sum
    while True:
        value = yield
        sum += value
        yield sum

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

    # Take four, with coroutine_example()
    cr = coroutine_example(starting_sum=7)
    # The following line could be send(None) as well.
    s = cr.next()  # Will yield sum from first time in loop.
    print "Starting value: {}".format(s)
    for i in range(10):
        sum = cr.send(i)
        print sum

    # Take four, with coroutine_example2()
    cr2 = coroutine_example2(starting_sum=13)
    s = cr2.next()
    print "Starting value: {}".format(s)
    for i in range(10):
        sum = cr2.send(i)
        print sum
    print "Done."

if __name__ == "__main__":
    sys.exit(main())
