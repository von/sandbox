#!/usr/bin/env python3
"""Examples of decorators"""

from functools import wraps
import inspect

class MyDecorator1(object):
    """Example of decorator using a class and __call__()

    Kudos: http://www.artima.com/weblogs/viewpost.jsp?thread=240808
    """
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(f"Calling decorated function {self.function.__name__}")
        self.function(*args, **kwargs)
        print(f"Exiting decorated function {self.function.__name__}")

def MyDecorator2(function):
    """Exacmple of decorator using a function"""
    # Lack of @wraps() here is intentional
    def new_function(*args, **kwargs):
        print(f"Calling decorated function {function.__name__}")
        function(*args, **kwargs)
        print(f"Exiting decorated function {function.__name__}")
    return new_function

class MyDecorator3(object):
    """Example of a decorator that can decorate a function or not depending
    on class state."""
    decoration_on = True

    @classmethod
    def do_decoration(cls, value=True):
        """Set whether or not decorate() decorates or not."""
        cls.decoration_on = value

    @classmethod
    def decorate(cls, function):
        """Decorate the function if decoration_on == True, otherwise
        return unmodified function."""
        if cls.decoration_on:
            @wraps(function)
            def new_function(*args, **kwargs):
                print("Decoration!")
                function(*args, **kwargs)
                print("End decoration!")
            return new_function
        else:
            return function

@MyDecorator1
def func1(msg):
    print(f"Inside func1({msg})")

@MyDecorator2
def func2(msg):
    print(f"Inside func2({msg})")

MyDecorator3.do_decoration(False)

@MyDecorator3.decorate
def func3(msg):
    print(f"Inside func3({msg})")

MyDecorator3.do_decoration(True)

@MyDecorator3.decorate
def func4(msg):
    print(f"Inside func4({msg})")

func1("Hello world")
func2("Goodbye world")
func3("Hello again")  # Should not be decorated
func4("Goodbye again")

print(f"Wrapped func2 without @wraps: {func2.__name__}")
print(f"Wrapped func4 with @wraps: {func4.__name__}")

######################################################################

def add_method(instance):
    """Add decorated function as method to given instance.

    Kudos: http://wiki.python.org/moin/PythonDecoratorLibrary#Easyaddingmethodstoaclassinstance
    """
    def decorator(f):
        import types
        f = types.MethodType(f, instance)
        setattr(instance, f.__name__, f)
        return f
    return decorator

class Foo:
    def __init__(self):
        self.x = 42

foo = Foo()

@add_method(foo)
def get_x(self):
    return self.x

print(f"foo.get_x() = {foo.get_x()}")

######################################################################

def class_decorator(cls):
    """Decorate a class"""
    def method(self):
        """Return the instance atttibute 'x'"""
        return self.x
    @classmethod
    def clsmethod(cls):
        """Return the class atttibute 'y'"""
        return cls.y
    @staticmethod
    def smethod():
        """Return the string 'foo'"""
        return "foo"

    # Wrap any existing methods starting with "some".
    # ismethod() doesn't work here, must use isfunction
    method_names = [name for name in cls.__dict__
                    if inspect.isfunction(cls.__dict__[name])]
    mod_method_names = [s for s in method_names if s.startswith("some")]

    def wrap_method(m):
        @wraps(m)
        def w(*args, **kwargs):
            print("Wrapped method!")
            m(*args, **kwargs)
        return w

    for method_name in mod_method_names:
        setattr(cls, method_name, wrap_method(cls.__dict__[method_name]))

    # Add some methods
    setattr(cls, method.__name__, method)
    # @classmethod and @staticmethod apparently don't set __name__
    # so we have to explicitly name the attibutes here
    setattr(cls, "clsmethod", clsmethod)
    setattr(cls, "smethod", smethod)

    return cls

@class_decorator
class Test(object):
    """Class to be decorated"""
    y = 99

    def __init__(self):
        self.x = 42

    def some_method(self):
        pass

t = Test()

print(f"t.method() = {t.method()} t.clsmethod = {t.clsmethod()} t.smethod = {t.smethod()}")

# Should print "Wrapped method!"
t.some_method()
