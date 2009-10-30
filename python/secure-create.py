#!/usr/bin/env python
"""Open a private file like a Globus proxy."""

import os

path="/tmp/secure-create.out"
if os.path.exists(path):
    os.remove(path)
# O_EXCL|O_CREAT to prevent a race condition where someone
# else opens the file first.
fd = os.open(path, os.O_WRONLY|os.O_CREAT|os.O_EXCL, 0600)
# Kudos: http://stackoverflow.com/questions/168559/python-how-do-i-convert-an-os-level-handle-to-an-open-file-to-a-file-object
file = os.fdopen(fd, "w")
file.write("Hello world")
file.close()
