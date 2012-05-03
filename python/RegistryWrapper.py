"""RegistryWrapper: class decorator that maps classes to keys"""

class RegistryWrapper(object):
    wrap_map = {}

    def __init__(self, wrapped_object):
        pass

    @classmethod
    def wrapped_class(cls, name):
        try:
            c = cls.wrap_map[name]
        except KeyError:
            c = None
        return c

    @classmethod
    def wrap(cls, name):
        def decorator(wrapping_cls):
            cls.wrap_map[name] = wrapping_cls
            return wrapping_cls
        return decorator

@RegistryWrapper.wrap("Hello")
class HelloWorld(object):
    pass

@RegistryWrapper.wrap("Good")
class GoodByeWorld(object):
    pass

print RegistryWrapper.wrapped_class("Good")
print RegistryWrapper.wrapped_class("Hello")
print RegistryWrapper.wrapped_class("Fail")


