#!/usr/bin/env python
"""Show any() and all() use in python

Because I keep forgetting what these methods are called."""

a = [0,1,2,3,4]
b = [1,2,3]
c = [0,0,0]

def demo(name, array):
    print "{}: {}".format(name, ",".join(map(str, array)))
    print "any({0}) = {1} all({0}) = {2}".format(name, any(array), all(array))

demo("a", a)
demo("b", b)
demo("c", c)

