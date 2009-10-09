#!/usr/bin/env python
import unittest

class FenwickTree:
    """Efficiently keep track of frequency counts and summing counts up
    a particular index. AKA a Binary Indexed Tree.

    Full dececription and much of this code based on:
    http://www.topcoder.com/tc?module=Static&d1=tutorials&d2=binaryIndexedTrees
    """
    
    # One trick used in this class is "index & -index" what this does
    # is to return a number that has only one bit set, that being the
    # lowest bit set in index. Here's why it works, think of index as
    # a10...0, that is some bitstring 'a' followed by a 1 and then some number 
    # of bits of value 0. -index would be ~index+1 or ~(a10...0) + 1
    # or ~a~1~0..0+1 or ~a01..1+1 or ~a10..0, so:
    # index & -index == a10..0 & ~a10..0 or 010..0

    # Type to feed into array constructor
    #  'I' for an integer, 'L' for a long or 'd' for a double.
    type = "I"

    def __init__(self, maxValue):
        """Create a new FenwickTree.

        maxIndex should be the maximum allowed index."""
        from array import array
        # We will use 1..maxVal for index, some increment to adjust for
        # Python's use of 0..maxVal-1
        maxValue += 1
        self.tree = array(self.type, [0] * maxValue)
        self.maxValue = maxValue

    def update(self, index, value):
        """Increase the count at index by value."""
        # Adjust indexing to start at 1
        index += 1
        while index <= self.maxValue:
            self.tree[index] += value
            # Shift index up to power of two above initial value and then
            # sift that bit to the left until we hit maxVal.
            index += index & -index

    def query(self, rangeTop):
        """Return sum of of range from rangeBottom to rangeTop inclusive."""
        # Adjust indexing to start at 1
        index = rangeTop + 1
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def querySingleValue(self, index):
        """Return the value at given position."""
        # Adjust indexing to start at 1
        index += 1
        sum = self.tree[index]
        # Zero is a special case that requires no further work
        if index > 0:
            # z is where index and index-1 cross, so we can quite counting
            # when we reach it
            z = index - (index & -index)
            index -= 1
            while index != z:
                sum -= self.tree[index]
                index -= index & -index
        return sum

    def scale(self, multiplier):
        """Scale all frequency counts by multiplier."""
        for i in xrange(1, self.maxValue):
            self.tree[i] *= multiplier

    def dump(self):
        """Dump tree to a string."""
        return " ".join(map(str, self.tree))

class FenwickTreeTests(unittest.TestCase):

    def testinit(self):
        tree = FenwickTree(512)

    def testquery(self):
        tree = FenwickTree(512)
        for i in range(512):
            tree.update(i, i)
        for i in range(512):
            expectedValue = i*(i+1)/2
            value = tree.query(i)
            self.assertEqual(expectedValue, value,
                             "Index %d: %d!=%d" % (i, expectedValue, value))

    def testquery2(self):
        tree = FenwickTree(512)
        for i in range(512):
            tree.update(i, i)
        # Increment count at zero by 10 whoch should propagate through
        # whole tree
        c = 10
        tree.update(0, c)
        for i in range(512):
            expectedValue = i*(i+1)/2 + 10
            value = tree.query(i)
            self.assertEqual(expectedValue, value,
                             "Index %d: %d!=%d" % (i, expectedValue, value))

    def testSingleValue(self):
        tree = FenwickTree(512)
        for i in range(512):
            tree.update(i, i)
        for i in range(512):
            value = tree.querySingleValue(i)
            self.assertEqual(value, i,
                             "Index %d: %d!=%d" % (i, i, value))

    def testScale(self):
        tree = FenwickTree(512)
        for i in range(512):
            tree.update(i, i)
        m = 5
        tree.scale(m)
        for i in range(512):
            expectedValue = i*(i+1)/2*m
            value = tree.query(i)
            self.assertEqual(expectedValue, value,
                             "Index %d: %d!=%d" % (i, expectedValue, value))


if __name__ == '__main__':
    unittest.main()

