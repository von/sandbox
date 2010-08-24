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
    # Take advantage of file being a generator here
    with file(argv[0]) as f:
        g = send_generator_to_coroutine(f, grep("while", printer("My output:")))
    print "Done."

if __name__ == "__main__":
    sys.exit(main())
