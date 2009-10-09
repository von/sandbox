#!/usr/bin/env python
from threading import *

class Test(Thread):

    def __init__(self):
	self.event = Event()
	Thread.__init__(self)

    def run(self):
	self.event.wait()
	print self.getName()

print "Start"
t1 = Test()
t2 = Test()
t1.start()
t2.start()
t2.event.set()
t1.event.set()
print "Done"
