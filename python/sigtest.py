#!/usr/bin/python
#
# Check to see if a signal interrupts a child thread reading a password
#
import getpass
import time
from threading import Thread

class PassReader(Thread):
    def run(self):
	print "password:"
	password = getpass.getpass()
	print password

p = PassReader();
p.start()

time.sleep(1000)

    
