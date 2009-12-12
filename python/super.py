#!/usr/bin/env python

class A(object):
    def routine(self):
        print "A.routine()"

class B(A):
    def routine(self):
        print "B.routine()"
        super(B, self).routine()

if __name__ == '__main__':
    a = A()
    b = B()
    print "Calling a.routine:"
    a.routine()
    print "Calling b.routine:"
    b.routine()
