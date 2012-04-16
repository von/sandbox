#!/usr/bin/env python
"""Demonstration of Python Abstract Base Classes

See: http://www.doughellmann.com/PyMOTW/abc/index.html
"""

import abc

#
# Our abstract base class
#
class Base(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def abstractmethod(self):
        """An abstract method that must be overridden"""
        return

    def do_something(self):
        """Abstract classes can non-abstract methods"""
        print "I do something!"

#
# A simple implementation
#

class Implementation(Base):
    def abstractmethod(self):
        """Implementation of abstract method"""
        self.do_something()

Implementation().abstractmethod()

#
# An incomplete implementation throws a type error
#

class IncompleteImplementation(Base):
    pass

try:
    # If you try to instantiate an incomplete implementation, you get a
    # TypeError
    IncompleteImplementation()
except TypeError:
    pass
else:
    print "Weird, creating an incomplete implementation didn't raise a TypeError"

#
# An implementation with register()
#

class Implementation2:
    """Example of using register() to register implementation

    One difference is that it won't appear in Base.__subclasses__()"""
    def abstractmethod(self):
        """Implementation of abstract method"""
        self.do_something()

Base.register(Implementation2)
# Will appear to be a subclass
print 'Registered is subclass:', issubclass(Implementation2, Base)
print 'Registered is instance:', isinstance(Implementation2(), Base)
try:
    # But it doesn't actually inherit
    Implementation2().abstractmethod()
except AttributeError:
    pass
except:
    print "Weird, registered class seems to have inheritied..."

#
# Incomplete impementation with register()
#
class IncompleteImplementation2:
    pass

Base.register(IncompleteImplementation2)
# But this doesn't see to raise any exception...
IncompleteImplementation2()

print "Success."

