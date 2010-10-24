#!/usr/bin/env python
"""Exploring python's 'with'

Kudos:
http://effbot.org/zone/python-with-statement.htm
http://www.doughellmann.com/PyMOTW/contextlib/

For context managers see:
http://docs.python.org/release/2.5.2/lib/typecontextmanager.html
http://docs.python.org/library/contextlib.html
http://www.python.org/dev/peps/pep-0343/
"""

from contextlib import contextmanager

class with_example:
    def hello(self):
        print "Hello world"

    def __enter__(self):
        print "Entering with block..."
        return self

    def __exit__(self, type, value, traceback):
        print "Exiting with block..."

with with_example() as thing:
    thing.hello()

# Do the same thing as above but with a context manager

@contextmanager
def context_manager_example():
    print "Entering context manager..."
    yield "World"
    print "Exiting context manager..."

with context_manager_example() as noun:
    print "Hello {}".format(noun)

#
# This block from:
# http://www.doughellmann.com/PyMOTW/contextlib/
@contextmanager
def make_context():
    print '  entering'
    try:
        yield {}
    except RuntimeError, err:
        print '  ERROR:', err
    finally:
        print '  exiting'

print 'Normal:'
with make_context() as value:
    print '  inside with statement:', value

print
print 'Handled error:'
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

print
print 'Unhandled error:'
try:
    with make_context() as value:
        raise ValueError('this exception is not handled')
except ValueError, e:
    print "ValueError not handled as expected: {}".format(e)
