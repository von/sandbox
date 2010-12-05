#!/usr/bin/env python
"""Demonstration of python inspect module (and a little bit of traceback).

http://blog.doughellmann.com/2007/11/pymotw-inspect.html
"""
import functools
import inspect
import sys
from optparse import OptionParser
import traceback

DIV = "\n\n" + "*"*70 + "\n\n"

def raise_exception():
    raise Exception("I am exceptional")

# A stack is a list or records.
#
# A record contains a frame object, filename, line number, function
# name, a list of lines of context, and index within the context

def print_records(records):
    """Print a set of records as returned by inspect.stack() or
    inspect.trace()"""
    for record in records:
        print_record(record)

def print_record(record):
    """Print a record as returned by inspect.stack() or
    inspect.trace()

    A record contains a frame object, filename, line number, function
    # name, a list of lines of context, and index within the context.

    Yes, a record seems to be very much like a frame."""
    print_frame(record[0])

def print_frame(frame):
    """Print a frame"""
    frameinfo = inspect.getframeinfo(frame)
    # A tuple of five things is returned: the filename, the line number of
    # the current line, the function name, a list of lines of context from
    # the source code, and the index of the current line within that list.
    print "  Frame: Function: {0.function} in {0.filename} line {0.lineno}"\
        .format(frameinfo)
    if frameinfo.code_context is not None:
        print "    ",frameinfo.code_context[0],
    else:
        print "    Looks like an eval() call",\
            "but I don't know how to get at more information"

def print_traceback(tb):
    """Print a traceback from inside an exception handler.

    By default, get traceback from current exception (sys.exc_info())

    Also see traceback.print_tb() and related functions."""
    inner_frames = inspect.getinnerframes(tb)
    outer_frames = inspect.getouterframes(tb.tb_frame)
    while tb is not None:
        print_frame(tb.tb_frame)
        # Traceback is linked list, with tb_next being the link
        tb = tb.tb_next
    print "Inner frames (the trace()):"
    print_records(inner_frames)
    print "Outer frames (the stack()):"
    print_records(outer_frames)

def print_function(function):
    spec = inspect.getargspec(function)
    print "Constructed piecemeal:"
    print inspect.getcomments(function),
    print "def {}({}, *{}, **{}):".format(
        function.__name__,
        args_to_string(spec.args, spec.defaults),
        spec.varargs,
        spec.keywords)  # Not varkw as in documentation
    print "    \"\"\"{}\"\"\"".format(inspect.getdoc(function))
    print "\nOr using formatargspec():"
    print "def {}{}:".format(
        function.__name__,
        inspect.formatargspec(spec.args, spec.varargs,
                              spec.keywords, spec.defaults))
    print "\nOr in one call with getsource():"
    print inspect.getsource(function)

def args_to_string(args, defaults=()):
    """Convert a set of argument names and default values to a string

    Hasn't been seriously tested for complicated values."""
    offset = len(args) - len(defaults)
    arg_strs = args[:offset]
    # use repr() (!r) in following line to get quoted strings for defaults
    arg_strs.extend(["{}={!r}".format(a,d)
                     for a,d in zip(args[offset:], defaults)])
    return ", ".join(arg_strs)

# Demo function
# These comments are available via inspect.getcomments()
def demo_function(something, foo=1, bar="two", d={},
                  *other_args, **other_kwargs):
    """This is a demo function for print_function()"""
    pass

class WeirdException(Exception):
    """Some new weird exception"""

def exception_changer(function, *args, **kwargs):
    """Change any exception to WeirdExceptions as a demonstration.

    Calls given function and changes its exceptions, but makes them still
    look like they came from the function."""
    try:
        function(*args, **kwargs)
    except Exception as ex:
        # Re-raise exception as ValueError with modified message and same
        # traceback as original exception.
        raise WeirdException, \
            "Modified message:" + ex.message + "!", \
            sys.exc_info()[2]

def exception_changing_decorator(function):
    """Change all exceptions from the wrapped function to WeirdException"""
    @functools.wraps(function)
    def f(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            raise WeirdException, e.message, sys.exc_info()[2]
            # Use 'raise' to just reraise exception without altering it.
    return f

@exception_changing_decorator
def exception_raiser_two():
    raise ValueError("A bogus ValueError")

def get_docstring():
    """Return the docstring of our caller

    We do this by looking up the caller's name, then map that to a function
    object using its globals and then use getdoc() to get the docstring."""
    caller_record = inspect.stack()[1]
    caller_frame = caller_record[0]
    frame_info = inspect.getframeinfo(caller_frame)
    # If we're being called by a class method, we might need to
    # look at cls.__dict__[frame_info.function] to get the method object.
    f = caller_frame.f_globals[frame_info.function]
    return inspect.getdoc(f)

def main(argv=None):
    """This is our main function"""
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    print DIV
    print "Part One: stack() and trace() demonstrations\n"
    print "Printing stack() from inside main():"
    print_records(inspect.stack())
    print "Printing trace() from inside main(): (will be empty)"
    print_records(inspect.trace())

    try:
        eval("raise_exception()")
    except Exception as ex:
        print "\nTraceback from inside exception handler:"
        print_traceback(sys.exc_info()[2])
        print DIV
        print "Printing stack() from inside exception handler:"
        print_records(inspect.stack())
        print "\nPrinting trace() from inside exception handler:"
        print "    (Will be the almost the same as traceback)"
        print_records(inspect.trace())

    print DIV
    print "Part two: inspect a function.\n"
    print_function(demo_function)

    print DIV
    print "Part three: modifying an exception"
    print "    (Really nothing to do with inspect directly)\n"
    try:
        exception_changer(raise_exception)
    except Exception as ex:
        traceback.print_exc()


    print "\nNow using a decorator:"
    try:
        exception_raiser_two()
    except Exception as ex:
        traceback.print_exc()

    print DIV
    print "Demonstrate returning the docstring of a caller.\n"
    print "My docstring is: ", get_docstring()
    
    print "\n\nThat's all folks.\n"

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        raise
    sys.exit(0)
