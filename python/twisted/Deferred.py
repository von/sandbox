#!/usr/bin/env python
"""Example of using a Deferred instance"""

import time

from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList, execute

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

def slow_answers(n):
    """Take a while to return an answer."""
    print "slow_answers() called..."
    time.sleep(5)
    print "slow_answers() returning..."
    return n*2
    
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

d = execute(slow_answers, 6)
d.addCallback(callback)

reactor.callLater(10, reactor.stop)
reactor.run()
