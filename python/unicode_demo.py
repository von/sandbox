#!/usr/bin/env python
"""Demonstrate Unicode

Key points:

    * Unicode is essentially an code for every character on earth.

    * UTF-8 is an encoding scheme, like ascii, but able to handle any character.
    It is efficient and in some sense a superset of ascii in that asci characters
    (0x00-0x7f) are encoded in one byte. Characters greater 0x7f are endocoded
    in 2-4 bytes, each byte being 0x80-0xff. UTF-8 is the dominate scheme
    used on the WWW.

    * One decode()s from UTF-8 into unicode and then encode()s from unicode
    into UTF-8.

    * Thile file doesn't have a coding magic string at the top, so python2
    will parse it as plain asci, meaning the file itself can't have utf-8
    characters in it. E.g. this line appearing on the second line of the file
    would tell python2 this file was utf-8:
        # -*- coding: utf-8 -*-

    * See unicode_demo_p3.py for python3 notes.

    Kudos:
    http://farmdev.com/talks/unicode/
    https://docs.python.org/2/howto/unicode.html
    https://home.unicode.org/
    https://en.wikipedia.org/wiki/Unicode
"""
from __future__ import print_function

# Unicode is a set of bytes
u = u'Ivan Krsti\u0107'
print("Hello", u, "- implicit conversion of ", type(u))

# Unicode gets encoded to strings
s = u.encode('utf-8')
print("Hello", s, "- converted to", type(s))

print("Decoded string matches original unicode:", u == s.decode('utf-8'))
print("Both string and unicode derive from basestring:",
      isinstance(s, basestring) and isinstance(u, basestring))

print("""
Proposed solution by http://farmdev.com/talks/unicode/:
    Decode early
    Unicode everywhere
    Encode late
""")
