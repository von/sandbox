#!/usr/bin/env python3
"""
Playing with Meta-classes.

Basically, my words, a meta-class is what is used to create a class.
Normally it is type.

Kudos:
http://www.voidspace.org.uk/python/articles/metaclasses.shtml
http://eli.thegreenplace.net/2012/04/16/python-object-creation-sequence/
"""

from types import FunctionType

class ClassWithoutMeta(object):
    """Class with no metaclass"""

    def __new__(cls, *args, **kwargs):
        obj = super(ClassWithoutMeta, cls).__new__(cls)
        print(('ClassWithoutMeta.__new__ called. got new obj id=0x%x' % id(obj)))
        return obj

    def __init__(self, arg):
        print(('ClassWithoutMeta.__init__ called (self=0x%x) with arg=%s' % (id(self), arg)))
        self.arg = arg

print("type(ClassWithoutMeta)=", type(ClassWithoutMeta))
t = ClassWithoutMeta("Hello World")
print()

######################################################################


class TestMetaClass(type):

    def __new__(meta, classname, bases, classDict):
        """Called to construct the TestWithMetaClass class itself"""
        obj = super(TestMetaClass, meta).__new__(meta, classname, bases, classDict)
        print(('TestMetaClass.__new__ called. got new obj id=0x%x' % id(obj)))
        return obj

    def __call__(cls, *args, **kwargs):
        """Called with TestWithMetaClass() called since it is of type TestMetaClass

        cls will be TestWithMetaClass"""
        print('TestMetaClass.__call__()')
        return cls.__new__(cls, *args, **kwargs)

class TestWithMetaClass(object, metaclass=TestMetaClass):

    def __new__(cls, *args, **kwargs):
        obj = super(TestWithMetaClass, cls).__new__(cls)
        print(('TestWithMetaClass.__new__ called. got new obj id=0x%x' % id(obj)))
        return obj

    def __init__(self):
        print(('TestWithMetaClass.__init__ called (self=0x%x) with arg=%s' % (id(self), arg)))

# type(TestWithMetaClass) is now TestMetaClass, so TestWithMetaClass()
# invokes TestWithMetaClass.__call__()
print("type(TestWithMetaClass)=", type(TestWithMetaClass))
t = TestWithMetaClass()
print("type(t)=", type(t))
print()

######################################################################

class AttributeDecorator(type):
    """A Meta-Class which creates get/set methods for all attributes."""

    def __new__(meta, classname, bases, classDict):
        for attributeName, attribute in list(classDict.items()):
            if type(attribute) != FunctionType:
                # Kudos: https://stackoverflow.com/q/24733831/197789
                exec(f"def getter(self): return self.{attributeName}",
                     globals())
                exec(f"def setter(self, value): self.{attributeName} = value",
                     globals())
                classDict["get_{}".format(attributeName)] = getter
                classDict["set_{}".format(attributeName)] = setter
        return type.__new__(meta, classname, bases, classDict)

class Test2(object, metaclass=AttributeDecorator):
    """This class will have get_*() and set_*() methods created for all
    of its attributes."""

    foo = 42

t = Test2()

print("foo={}".format(t.get_foo()))
t.set_foo(30)
print("foo={}".format(t.get_foo()))
