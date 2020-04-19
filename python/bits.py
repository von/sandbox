#!/usr/bin/env python3
"""Bit manipulation

Kudos http://wiki.python.org/moin/BitManipulation
"""
import sys

class Bits(int):
    def bitCount(self):
        count = 0
        value = self
        while (value):
            value &= value - 1
            count += 1
        return count

    def lowestSet(self):
        """Returns offset of lowest bit set."""
        low = (self & -self)
        lowBit = -1
        while (low):
            low >>= 1
            lowBit += 1
        return(lowBit)

    # testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.
    def testBit(self, offset):
        mask = 1 << offset
        return(self & mask)

    # setBit() returns an integer with the bit at 'offset' set to 1.
    def setBit(self, offset):
        print(self)
        self |= 1 << offset
        print(f"post: {self}")

    # clearBit() returns an integer with the bit at 'offset' cleared.
    def clearBit(self, offset):
        self &= ~(1 << offset)

    # toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.
    def toggleBit(self, offset):
        self ^= 1 << offset

    def __str__(self):
        if self == 0:
            return '0'
        s=''
        t={'0':'000','1':'001','2':'010','3':'011',
           '4':'100','5':'101','6':'110','7':'111'}
        for c in oct(self)[1:]:
                s+=t[c]
        return s

def main(argv=None):
    binaryValue = '0011010100'
    print(f"Value is {binaryValue}")
    b = Bits(int(binaryValue, 2))
    print(f"bitCount is {b.bitCount()}")
    print(f"lowestSet is {b.lowestSet()}")

    b = Bits(0)
    b.setBit(4)
    print(f"Value is {b}")
    print(f"bitCount is {b.bitCount()}")
    print(f"lowestSet is {b.lowestSet()}")

if __name__ == "__main__":
    sys.exit(main())
