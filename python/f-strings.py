#!/usr/bin/env python3
"""Demonstrate use of new Python 3.6+ f-strings

https://www.python.org/dev/peps/pep-0498/
"""

print("A python f-string renames parameters with coorsponding variable names.")
name = "world"
print(f"Hello {name}!")

print("They can also include expressions:")
a = 5
b = 10
print(f"{a} + {b} = {a + b}")


# One way to count, with a class
class Counter:
    def __init__(self):
        self.v = 1

    def __call__(self):
        r = self.v
        self.v += 1
        return r


counter = Counter()
print(f"{counter()} {counter()} {counter()}")


# Another way to count, with a closure
# Kudos: https://stackoverflow.com/a/1261952/197789
def make_counter(start=1):
    count = start

    def counter():
        nonlocal count
        r = count
        count += 1
        return r
    return counter


counter = make_counter(4)
print(f"{counter()} {counter()} {counter()}")

# Show formatting
print(f"{counter():02d} {counter():03d} {counter():04d}")
