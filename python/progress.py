#!/usr/bin/env python3
# Display updating progress on the terminal on a single line.
# http://stackoverflow.com/a/3173338

import time
import sys


print("Python2 version with write()...")
for i in range(5):
    time.sleep(1)
    # '\r' is carriage return without line feed
    # Need to use write() instead of print() as flush keyword
    # isn't supported until 3.3
    sys.stdout.write("\r{}%".format(i + 1))
    sys.stdout.flush()
sys.stdout.write("\n")  # Move to next line

print("Python3 version with print()...")
for i in range(5):
    time.sleep(1)
    # '\r' is carriage return without line feed
    print(f"{i+1}%", end='\r', flush=True)
sys.stdout.write("\n")  # Move to next line
