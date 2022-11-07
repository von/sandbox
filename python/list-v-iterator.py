#!/usr/bin/env python3
"""Show differences between list and itereator."""

import itertools

iter = itertools.repeat(10, 5)
list = list(iter)

print("len() doesn't work on iterators...")
try:
    print(f"len(iter) = {len(iter)}")
except TypeError:
    print("len(iter) failed")
print(f"len(list) = {len(list)}")

if 10 in iter:
    print("10 is in iter")
else:
    print("10 apparently not in iter")
if 10 in list:
    print("10 is in list")
else:
    print("10 apparently not in list")
