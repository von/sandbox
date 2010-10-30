#!/usr/bin/env python
"""
Playing with Meta-classes.

Basically, my words, a meta-class is what is used to create a class.
Normally it is type.

Kudos: http://www.voidspace.org.uk/python/articles/metaclasses.shtml
"""

from types import FunctionType

class MetaClass(type):
    def __new__(meta, classname, bases, classDict):
        print 'Creating new class: {}'.format(classname)
        return type.__new__(meta, classname, bases, classDict)

class Test(object):
    """Just creating this class will case MetaClass.__new__() to be invoked
    and "Creating new class: Test" to be printed."""

    __metaclass__ = MetaClass

    def __init__(self):
        pass

    def method(self):
        pass

    classAttribute = 'Something'

######################################################################

class AttributeDecorator(type):
    """A Meta-Class which creates get/set methods for all attributes."""

    def __new__(meta, classname, bases, classDict):
        for attributeName, attribute in classDict.items():
            if type(attribute) != FunctionType:
                exec("def getter(self): return self.{}".format(attributeName))
                exec("def setter(self, value): self.{} = value".format(attributeName))
                classDict["get_{}".format(attributeName)] = getter
                classDict["set_{}".format(attributeName)] = setter
        return type.__new__(meta, classname, bases, classDict)

class Test2(object):
    """This class will have get_*() and set_*() methods created for all
    of its attributes."""

    __metaclass__ = AttributeDecorator

    foo = 42

t = Test2()

print "foo={}".format(t.get_foo())
t.set_foo(30)
print "foo={}".format(t.get_foo())

