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
import os
import sys

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

print """
######################################################################
"""

class stdout_to_pipe(object):
    def __enter__(self):
        self.saved_stdout = sys.stdout
        read_fd, write_fd = os.pipe()
        reader = os.fdopen(read_fd)
        writer = os.fdopen(write_fd, "w", 0)  # 0 == unbuffered
        sys.stdout = writer
        return reader

    def __exit__(self, type, value, traceback):
        sys.stdout = self.saved_stdout

class pipe_to_stdin(object):
    def __enter__(self):
        self.saved_stdin = sys.stdin
        read_fd, write_fd = os.pipe()
        reader = os.fdopen(read_fd)
        writer = os.fdopen(write_fd, "w", 0)  # 0 == unbuffered
        sys.stdin = reader
        return writer

    def __exit__(self, type, value, traceback):
        sys.stdin = self.saved_stdin

with stdout_to_pipe() as out:
    print "Hello from stdout_as_pipe()!"
    a = out.readline()

print "Captured output: " + a

with pipe_to_stdin() as input:
    input.write("Hello world!\n")
    print "Captured input: " + sys.stdin.readline()
