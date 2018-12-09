#!/usr/bin/env python
"""Demonstrate __get__"""

class ArraySim:
    """Simple demo of __getitem__ to simulate array"""
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

class DictSim:
    """Simple demo of __getitem__ and __setitem__ to simulate dict"""
    def __init__(self):
        self.value = {}

    def __getitem__(self, name):
        if self.value.has_key(name):
            return self.value[name]
        else:
            return name.capitalize()

    def __setitem__(self, name, value):
        self.value[name] = value

a = ArraySim()
print "a[2]="+str(a[2])
print "a[3,5]="+str(a[3:5])
print "a[4:7]="+str(a[4:7])
print "a[0:5:2]="+str(a[0:5:2])

b = DictSim()
print b["hello"],b["world"]
b["world"] = "There"
print b["hello"],b["world"]

