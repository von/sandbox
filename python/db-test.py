#!/usr/bin/env python

import sys

class DB:
    def __init__(self, filename):
	import dbhash
	self.db = dbhash.open(filename, "c")

    def getValue(self, key):
	if self.db.has_key(key):
	    return self.db[key]
	else:
	    return None

    def setValue(self, key, value):
	self.db[key] = value

    def getInt(self, key, default=None):
	if self.db.has_key(key):
	    return int(self.db[key])
	elif default is not None:
	    return default
	else:
	    return None

    def setInt(self, key, value):
	self.db[key] = str(value)

name = sys.argv.pop()

db = DB("/tmp/testdb")

count = db.getInt("count", default=0)

value = db.getInt(name)

if value is not None:
    print "Existing value %d" % value
else:
    count += 1
    print "New value %d" % count
    db.setInt(name, count)
    db.setInt("count", count)
    
