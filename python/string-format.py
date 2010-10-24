#!/usr/bin/env python
"""Just me learning the new string formatting.

http://docs.python.org/library/string.html#formatstrings
"""
import string

print "Hello {1}, this is a {0}".format("test", "World")

# Automatic numbering available >= 2.7
print "Hello {}, this is a {}".format("World", "test")

print "Hello {target}, this is a {noun}".format(target="World",
                                                noun="test")
class A:
    def __init__(self, target, noun):
        self.target = target
        self.noun = noun

a = A(target="World", noun="test")

print "Hello {0.target}, this is a {0.noun}".format(a)

class B:
    def __init__(self, target):
        self.target = target

    def __str__(self):
        return "{} as a str".format(self.target)

    def __repr__(self):
        return "{} as a repr".format(self.target)

b = B("World")

print "str: {0!s}\nrepr: {0!r}".format(b)

class C:
    """When passed to format() just returns format_spec capitalized"""
    def __format__(self, format_spec):
        """http://www.python.org/dev/peps/pep-3101/"""
        return string.capwords(format_spec)

c = C()

print "c: {:hello world}".format(c)
