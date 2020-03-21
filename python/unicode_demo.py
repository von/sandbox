#!/usr/bin/env python
"""Demonstrate Unicode

Kudos: http://farmdev.com/talks/unicode/"""

# Unicode is a set of bytes
u = u'Ivan Krsti\u0107'

# Unicode gets encoded to strings
s = u.encode('utf-8')

print s

print "Implicit conversion:", u

# And strings decode into unicode
u2 = s.decode('utf-8')

print "u == u2?", u == u2

print """
Proposed solution by http://farmdev.com/talks/unicode/:
    Decode early
    Unicode everywhere
    Encode late
"""
