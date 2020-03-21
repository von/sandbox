#!/usr/bin/env python3
"""
Example of unicode abd utf-8 in python3, which has native unicode support.
E.g. this file doesn't need to tell python3 it is utf-8 encoded.

See unicode_demo.py for python2 and some background.

See also:
https://docs.python.org/3/howto/unicode.html
https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#unicode
"""

s = "Ivan Krstić"
print(type(s), "may now contain unicode:")
print("Hello", s)

b = s.encode("utf-8")
print("Python3 now has", type(b), "e.g.:", b)
s = b.decode("utf-8")
print("Which can be decoded to", type(s), ":", s)

s2 = "Ivan Krsti\u0107"
print("You can still use unicdoe literals, e.g.", s2)
