#!/usr/bin/env python
"""How to reraise a python exception and keep the original stacktrace
and a modified message."""

import sys


class ExceptionHolder:
    """Raise an exception, hold it and then re-raise it with original stack
    trace and a modified modify the message.

    Kudos:
    http://nedbatchelder.com/blog/200711/rethrowing_exceptions_in_python.html
    http://blog.ianbicking.org/2007/09/12/re-raising-exceptions/
    """
    def part_one(self):
        """Create exception but hold it."""
        try:
            raise RuntimeError("Hello World!")
        except Exception:
            self.exc_info = sys.exc_info()

    def part_two(self):
        """Throw exeception generated in part_one with modified message.

        This exception will seem to come from part_one()."""
        exc_class, exc, tb = self.exc_info
        # Create new exception as original class and modified message
        new_exc = exc_class("Re-raised exception: %s"
                            % (exc or exc_class))
        raise self.exc_info[0], new_exc, self.exc_info[2]

eh = ExceptionHolder()
eh.part_one()
eh.part_two()
