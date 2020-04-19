#!/usr/bin/env python3
import unittest

class HeapList(list):
    """Heap based on list data structure.

    A Heap is a tree in which a parent is always greater than
    its children and the tree is always filled left to right.
    Nodes can be any data element as long as comparison works."""

    def __init__(self, initial=None):
        """Create a HeapList.

        Initial should be a list of inital values for the list.
        Note that build() must be called if inital is not a legal heap."""
        if initial:
            self.extend(initial)
        self._size = None

    def size(self):
        """Return size of heap. This is same as len unless size has been set."""
        if self._size: return self._size
        return len(self)

    def left(self, index):
        """Return index of left child or None if no child."""
        childIndex = (index<<1) + 1
        if childIndex >= self.size(): return None
        return childIndex

    def right(self, index):
        """Return index of right child or None if no child."""
        childIndex = (index<<1) + 2
        if childIndex >= self.size(): return None
        return childIndex

    def parent(self, index):
        """Return index of parent or None if root node."""
        if index == 0: return None
        return (index-1)>>1

    def height(self):
        """Return height, or the number of levels of leaves."""
        from math import log
        return int(log(self.size(), 2))

    def swap(self, i1, i2):
        """Swap i1 and i2."""
        (self[i2],self[i1]) = (self[i1],self[i2])

    def add(self, n):
        """Add a node maintaining heap."""
        if self._size:
            if len(self) > self._size:
                self[len(self)] = n
            else: # Assume self.size = len(self)
                self.append(n)
            self._size += 1
        else:
            self.append(n)
        i = self.size() - 1
        p = self.parent(i)
        while p and (self[i] > self[p]):
            self.swap(i,p)
            (i,p) = (p,self.parent(p))

    def heapify(self, i=0):
        """Float the value at index i down until we have a legal heap.

        Assumes rest of heap (below i) is legal heap."""
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l and self[l] > self[i]:
            largest = l
        if r and self[r] > self[largest]:
            largest = r
        if largest != i:
            self.swap(i,largest)
            self.heapify(largest)

    def build(self, size=None):
        """Construct legal heap assuming nothing and initial state.

        If size is not None, specifies size of heap, otherwise len(self) is used."""
        if size: assert(size > len(self))
        self._size = size
        for i in range(int(self.size()/2), -1, -1):
            self.heapify(i)

    def check(self, i=0):
        """Are we a legal heap? Returns True or False."""
        # We don't need to check for balance since array implementation
        # guarantees this.
        l = self.left(i)
        r = self.right(i)
        for child in [l,r]:
            if child and (self[i] < self[child] or not self.check(child)):
                return False
        return True

    def sort(self):
        """Use heapsort to sort value into ascending order.

        Assumes heap is legal."""
        saveSize = self._size
        if not self._size: self._size = len(self)
        for i in range(self.size() - 1, 0, -1):
            # Move largest element to last position
            self.swap(0, i)
            # Remove last position from heap
            self._size -= 1
            # And bubble up new largest element to top of heap
            self.heapify()
        self._size = saveSize

class HeapListTests(unittest.TestCase):

    def testinit(self):
        heap = HeapList()
        self.assertEqual(heap.size(), 0)
        heap = HeapList(list(range(7)))
        self.assertEqual(heap.size(), 7)

    def testleft(self):
        heap = HeapList(list(range(6)))
        self.assertEqual(heap.left(0),1)
        self.assertEqual(heap.left(1),3)
        self.assertEqual(heap.left(2),5)
        self.assertEqual(heap.left(3),None)

    def testright(self):
        heap = HeapList(list(range(6)))
        self.assertEqual(heap.right(0),2)
        self.assertEqual(heap.right(1),4)
        self.assertEqual(heap.right(2),None)

    def testparent(self):
        heap = HeapList(list(range(6)))
        self.assertEqual(heap.parent(0),None)
        self.assertEqual(heap.parent(1),0)
        self.assertEqual(heap.parent(2),0)
        self.assertEqual(heap.parent(3),1)
        self.assertEqual(heap.parent(4),1)
        self.assertEqual(heap.parent(5),2)

    def testheight(self):
        heap = HeapList(list(range(1)))
        self.assertEqual(heap.height(), 0)
        heap = HeapList(list(range(2)))
        self.assertEqual(heap.height(), 1)
        heap = HeapList(list(range(6)))
        self.assertEqual(heap.height(), 2)
        heap = HeapList(list(range(45)))
        self.assertEqual(heap.height(), 5)

    def testswap(self):
        heap = HeapList(list(range(5)))
        heap.swap(0,1)
        self.assertEqual(heap[0], 1)
        self.assertEqual(heap[1], 0)
        heap.swap(1,2)
        self.assertEqual(heap[2], 0)
        self.assertEqual(heap[1], 2)

    def testadd(self):
        heap = HeapList([20-2*i for i in range(4)])
        heap.add(19)
        self.assertEqual(heap[1], 19)
        self.assertEqual(heap[4], 18)

    def testheapify(self):
        heap = HeapList([20-2*i for i in range(4)])
        heap[0] = 10
        heap.heapify(0)
        self.assertEqual(heap[0], 18)
        self.assertEqual(heap[1], 14)
        self.assertEqual(heap[2], 16)  # Shouldn't have changed
        self.assertEqual(heap[3], 10)

    def testcheck(self):
        heap = HeapList(list(range(10)))
        self.assertFalse(heap.check())
        heap = HeapList([20-i for i in range(20)])
        self.assertTrue(heap.check())

    def testbuild(self):
        from random import shuffle
        heap = HeapList(list(range(100)))
        shuffle(heap)
        heap.build()
        self.assertTrue(heap.check())

    def testsort(self):
        from random import shuffle
        heap = HeapList(list(range(100)))
        shuffle(heap)
        heap.build()
        self.assertTrue(heap.check())
        heap.sort()
        for i in range(heap.size()-1):
            self.assertTrue(heap[i] < heap[i+1])

if __name__ == '__main__':
    unittest.main()
