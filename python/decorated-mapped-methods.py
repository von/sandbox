#!/usr/bin/env python
"""Demonstrate use of decorators to map methods to functions and methods.

Kudos: http://www.scribd.com/doc/39946630/Python-Idioms (slides 9-10)
Example does this with classes, this does it with functions.
"""

class Mapper(object):
    mappings = {}

    # Decorator with arguments. Note this gets called twice, first with
    # arguments and then with function to be wrapped. Hence it creates
    # and returns a decorator.
    # Kudos: https://speakerdeck.com/dabeaz/python-3-metaprogramming?slide=47
    @classmethod
    def register(cls, *names):
        """Create a mapping between decorated function and given names"""
        def decorator(function):
            for name in names:
                cls.mappings[name] = function
            return function
        return decorator

    @classmethod
    def get_by_name(cls, name):
        """Return function associated with given name"""
        return cls.mappings.get(name)

    @classmethod
    def invoke_by_name(cls, name, *args, **kw):
        """Invoke the gunction associated with given name with given arguments"""
        cls.mappings.get(name)(*args, **kw)

@Mapper.register("foo", "bar")
def do_foo(*args, **kw):
    print "do_foo() called."
    print "Args: " + " ".join(args)

Mapper.get_by_name("foo")()
Mapper.invoke_by_name("bar", "fie", "foe", "fum")

