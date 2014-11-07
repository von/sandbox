#!/usr/bin/env python
# encoding: utf-8
#
# Display updating progress on the terminal on a single line.
# http://stackoverflow.com/a/3173338

import time
import sys


for i in range(100):
    time.sleep(1)
    # '\r' is carriage return without line feed
    # Need to use write() instead of print() as flush keyword
    # isn't supported until 3.3
    sys.stdout.write("\r{}%".format(i + 1))
    sys.stdout.flush()
sys.stdout.write("\n")  # Move to next line
