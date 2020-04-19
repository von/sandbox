#!/usr/bin/env python3
"""Demonstrate use of importlib to load source

Was imp.load_source() in Python2"""

import argparse
import importlib.util
import sys

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    module_name="demo"
    file_path="./importlib-load-source-obj.py"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    c = module.MyClass()
    c.doit()

if __name__ == "__main__":
    sys.exit(main())
