#!/usr/bin/env python
"""Show use of callbacks from one call to another."""

class One:
    def main(self):
        t = Two(callback = self.callback)
        t.doit()

    def callback(self, value):
        print "Callback invoked with value = %s" % value

class Two:
    def __init__(self, callback):
        self.callback = callback

    def doit(self):
        callback = self.callback
        callback("Hello world!")
        self.callback("Should still be 'Hello world!'")

if __name__ == "__main__":
    one = One()
    one.main()
