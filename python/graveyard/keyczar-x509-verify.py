#!/usr/bin/env python
"""Use keyczar to verify a X509 certificate"""

import sys

import keyczar.util

def main(argv=None):
    if argv is None:
        argv = sys.argv
    x509_file = argv[1]
    with open(x509_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # Strip first and last lines with are "BEGIN" and "END" lines
    x509_pem = "".join(lines[1:-1])
    print x509_pem

    bytes = keyczar.util.Decode(x509_pem)
    x509 = keyczar.util.ParseX509(x509_pem)

if __name__ == "__main__":
    sys.exit(main())
