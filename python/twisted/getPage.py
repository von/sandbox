#!/usr/bin/env python
"""Demonstration of getPage"""

from twisted.internet import reactor
from twisted.web.client import getPage
from twisted.python.util import println
import sys

def print_page(data):
    println(data)
    reactor.stop()

def print_error(error):
    println("Error:",error)
    reactor.stop()

try:
    url = sys.argv[1]
except:
    url = "http://www.google.com/"

print "Getting", url

d = getPage(url)

d.addCallbacks(callback=print_page,
               errback=print_error)
reactor.run()
