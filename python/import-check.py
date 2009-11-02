#!/usr/bin/env python

try:
    import foo
except:
    print "Import of foo failed."

try:
    import os
except:
    print "Import of os failed."

print "Process pid is %d" % os.getpid()
