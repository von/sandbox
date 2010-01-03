#!/usr/bin/env python
#
# How to reraise a python exception and keep the original stacktrace.

import sys

class ExceptionHolder:
    """Raise an exception hold it and then re-raise it with original stack trace.

    Kudos:
    http://nedbatchelder.com/blog/200711/rethrowing_exceptions_in_python.html
    http://blog.ianbicking.org/2007/09/12/re-raising-exceptions/
    """
    def part_one(self):
        """Create exception but hold it."""
        try:
            raise Exception("Hello World!")
        except Exception, ex:
            self.exc_info = sys.exc_info()

    def part_two(self):
        """Throw exeception generated in part_one."""
        # This exception will seem to come from part_one()
        raise self.exc_info[0], self.exc_info[1], self.exc_info[2]

eh = ExceptionHolder()
eh.part_one()
eh.part_two()

        
