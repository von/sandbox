#!/usr/bin/env python3
"""Demonstrate collections.Counter for letter frequency analysis"""

import collections
import string

s = (" Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
     " nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,"
     " sed diam voluptua. At vero eos et accusam et justo duo dolores et ea"
     " rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem"
     " ipsum dolor sit amet.")

print("Lorem ipsum:")
c = collections.Counter(s.lower())
for letter, num in sorted(c.items(), key=lambda i: i[1], reverse=True):
    if letter in string.ascii_lowercase:
        print(f"{letter}: {num}")

print("Dictionary:")
c = collections.Counter()
with open("/usr/share/dict/words") as f:
    for word in f.readlines():
        c.update(word.strip().lower())

for letter, num in sorted(c.items(), key=lambda i: i[1], reverse=True):
    if letter in string.ascii_lowercase:
        print(f"{letter}: {num}")
