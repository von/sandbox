#!/usr/bin/env python3
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
    a generator.

    This particular generate never stops unless close()ed"""
    print("Hello world! I'm a generator.")
    i = 1
    try:
        while True:
            yield "I generated %d" % (i * n)
            i += 1
    except GeneratorExit:
        print("Generator closed at i=%d" % i)


def main(argv=None):
    print("Creating generator. Nothing should be printed here...")
    gen = my_generator(10)

    print("Calling generator.next(). This should print 'Hello world!'")
    s = next(gen)

    print("Calling generator.next() 10 more times. Should not print 'Hello world!'")
    for i in range(10):
        print(next(gen))
    gen.close()

    print("Creating generator via expression")
    gen_exp = (x*x for x in range(10))

    print("Using generator from expression")
    for i in gen_exp:
        print(i)

    print("Slightly more fun generator expression" \
        " that only does even numbers...")
    gen_exp = (x*x for x in range(10) if x%2 == 0)
    for i in gen_exp:
        print(i)

    return(0)


if __name__ == "__main__":
    sys.exit(main())
