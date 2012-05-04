#!/usr/bin/env python
# Kudos:
# http://stackoverflow.com/a/1695250/197789
#
# I like this method because you can assign arbitrary values to the enums

def enum(**enums):
    return type('Enum', (), enums)

Numbers = enum(ONE=1, TWO=2, THREE='three')
print Numbers.ONE
print Numbers.TWO
print Numbers.THREE

# Creating multiple types with the same name doesn't cause a problem.

GermanNumbers = enum(ONE="Eins", TWO="Zwei", THREE='Drei')
print GermanNumbers.ONE
print GermanNumbers.TWO
print GermanNumbers.THREE

# An alternative with no function
NUMBERS = type('NumbersEnum', (), {
    "ONE":1,
    "TWO":2,
    "THREE":3,
    })

print NUMBERS.ONE
print NUMBERS.TWO
print NUMBERS.THREE

