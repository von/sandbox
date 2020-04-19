"""mymockdemo: Demo code for mock_demo.py"""

import os
import os.path


def rm(path):
    """A wrapper around os.remove()"""
    if os.path.isfile(path):
        os.remove(path)
