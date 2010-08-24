#!/usr/bin/env python
"""Demonstrate generator

Kudos: David Beazley http://www.dabeaz.com/generators/
"""

import sys

def my_generator(n):
    """A generator.

    The key thing to realize is that this function when invoked does not
    actually execute, it returns a generator that produces results when
    the next() method is called.

    The fact the function contains a yield statement causes it to be
    a generator."""
    print "Hello world! I'm a generator."
    i = 1
    while True:
        yield "I generated %d" % (i * n)
    # This particular generate never stops


def main(argv=None):
    print "Creating generator. Nothing should be printed here..."
    gen = my_generator(10)

    print "Calling generator.next(). This should print 'Hello world!'"
    s = gen.next()

    print "Calling generator.next() 10 more times. Should not print 'Hello world!'"
    for i in range(10):
        print gen.next()
        
    return(0)


if __name__ == "__main__":
    sys.exit(main())


        
