#!/usr/bin/env python

try:
    import foo
except ImportError, e:
    print "Import of foo failed: %s" % e

try:
    import os
except  ImportError, e:
    print "Import of os failed."

print "Successfully imported 'os'"
print "Process pid is %d" % os.getpid()
