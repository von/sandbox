#!/usr/bin/env python
"""Demonstrate __getitem__"""

class A:
    """Simple defmo of __getitem__"""
    def __getitem__(self, i):
        if isinstance(i, slice):
            print i.start, i.stop, i.step
            args = [i.start] if i.start is not None else []
            args.append(i.stop)
            if i.step:
                args.append(i.step)
            print args
            return [v*2 for v in range(*args)]
        else:
            return i*2

a = A()
print "a[2]="+str(a[2])
print "a[3,5]="+str(a[3:5])
print "a[4:7]="+str(a[4:7])
print "a[0:5:2]="+str(a[0:5:2])
        
