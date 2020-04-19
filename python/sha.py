#!/usr/bin/env python3
"""An example python hashing application.

%prog <file to hash>
"""
import hashlib
from optparse import OptionParser
import sys

BLOCK_SIZE=1024

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv
    parser = OptionParser(
        usage=__doc__, # printed with -h/--help
        version="%prog 1.0" # automatically generates --version
        )
    (options, args) = parser.parse_args()
    if len(args) == 0:
        parser.error("Missing filename")
    for filename in args:
        hash = hashlib.sha1()
        with open(filename) as f:
            while True:
                data = f.read(BLOCK_SIZE)
                if not data:
                    break
                hash.update(data.encode("utf-8"))
            print(f"{filename}: {hash.hexdigest()}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
