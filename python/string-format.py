#!/usr/bin/env python3
"""Just me learning the new string formatting.

http://docs.python.org/library/string.html#formatstrings
"""
import string

print("Hello {1}, this is a {0}".format("test", "World"))

# Automatic numbering available >= 2.7
print("Hello {}, this is a {}".format("World", "test"))

print("Hello {target}, this is a {noun}".format(target="World",
                                                noun="test"))
class A:
    def __init__(self, target, noun):
        self.target = target
        self.noun = noun

a = A(target="World", noun="test")

print("Hello {0.target}, this is a {0.noun}".format(a))

class B:
    def __init__(self, target):
        self.target = target

    def __str__(self):
        return "{} as a str".format(self.target)

    def __repr__(self):
        return "{} as a repr".format(self.target)

b = B("World")

print("str: {0!s}\nrepr: {0!r}".format(b))

class C:
    def __init__(self):
        self.i = 0

    """When passed to format() just returns format_spec capitalized"""
    def __format__(self, format_spec):
        """http://www.python.org/dev/peps/pep-3101/"""
        return string.capwords(format_spec)

    @property
    def dynamic(self):
        """Return an incrementing number"""
        self.i += 1
        return self.i

c = C()
print("c: {:hello world}".format(c))
print("c: {c.dynamic} {c.dynamic} {c.dynamic}".format(c=c))

# Formatting of named placeholders
# Take i, right align (>), and pad with 0  to length 2
print("{c.dynamic:0>2}".format(c=c))

class D:
    """Run the format_spec as python code

    WARNING: Not to be used with untrusted format_specs

    This may not be a good idea, just exploring what is possible.

    Note that this won't handle multi-command/multi-line code as
    that requires exec() and complexity to get the output.
    See https://stackoverflow.com/a/52361938/197789"""
    def __format__(self, format_spec):
        """http://www.python.org/dev/peps/pep-3101/"""
        return str(eval(format_spec))

d = D()
print("d: {d:4+5}".format(d=d))
