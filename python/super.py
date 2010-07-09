#!/usr/bin/env python
#
# Kudos: http://stackoverflow.com/questions/576169/python-super
#

class A(object):
    def routine(self):
        print "A.routine()"

class B(A):
    def routine(self):
        print "B.routine()"
        # Note that the following error:
        # "super() argument 1 must be type, not classobj"
        # Means the super class is a classic class (i.e. not rooted at
        # object) and super won't work. You have to use the class name
        # explicitly.
        # Kudos: http://www.velocityreviews.com/forums/t338909-help-with-super.html
        super(B, self).routine()

if __name__ == '__main__':
    a = A()
    b = B()
    print "Calling a.routine:"
    a.routine()
    print "Calling b.routine:"
    b.routine()
