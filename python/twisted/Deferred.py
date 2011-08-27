#!/usr/bin/env python
"""Example of using a Deferred instance"""

from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList

def defered_answer(x):
    """Returns a defered whose callback will be called multiple times."""
    d = Deferred()
    reactor.callLater(x, # When
                      d.callback, # What
                      x*2) # Value
    return d

def defered_answers(n):
    """Returns a defered whose callback will be called multiple times."""
    ds = []
    for i in range(n):
        d = defered_answer(i)
        ds.append(d)
    dl = DeferredList(ds)
    return dl

def callback(d):
    """Prints data"""
    print "Callback:", d

def list_callback(results):
    for (success, value) in results:
        if success:
            print "List callback:", value
        else:
            print "List callback got an error."

d = defered_answer(4)
d.addCallback(callback)

dl = defered_answers(3)
dl.addCallback(list_callback)

reactor.callLater(5, reactor.stop)
reactor.run()
